import json
from datetime import date, datetime
from typing import Optional

from desktop_app.dao.database import DAO
from desktop_app.models.livro import Livro
from desktop_app.models.editora import Editora


class LivroDAO(DAO):
    """
    DAO for Livro using MSSQL.

    Uses the base DAO class for:
    - connection
    - cursor
    - config loading
    """

    TABLE_NAME = "Livro"

    def __init__(self):
        super().__init__()

    # ---------------------------------------------------------
    # Internal helpers
    # ---------------------------------------------------------

    @staticmethod
    def _list_to_db(value: list | None) -> str:
        """
        Converts Python list to JSON string for database storage.
        To be used for fields like "Tipo" and "Tema"
        """
        return json.dumps(value or [], ensure_ascii=False)

    @staticmethod
    def _list_from_db(value: str | None) -> list:
        """
        Converts JSON string from database back to Python list.
        To be used for fields like "Tipo" and "Tema"
        """
        if not value:
            return []

        try:
            result = json.loads(value)
            if isinstance(result, list):
                return result
            return [result]
        except json.JSONDecodeError:
            return []

    @staticmethod
    def _editora_id(editora: Editora | None):
        """
        Extracts Editora ID if available.

        """
        if editora is None:
            return None

        if hasattr(editora, "nipc"):
            return editora.get_id()

        if hasattr(editora, "get_id"):
            return editora.get_id() 

        return None

    @staticmethod
    def _row_to_livro(row) -> Livro:
        """
        Converts a database row into a Livro object.
        """

#        data_publicacao = row.Data_Publicacao

#        if isinstance(data_publicacao, datetime):
#            data_publicacao = data_publicacao.date()

        return Livro(
            ISBN=row.ISBN,
            Titulo=row.Titulo,
            idioma=row.Idioma,
            tipo=LivroDAO._list_from_db(row.Tipo),
            tema=LivroDAO._list_from_db(row.Tema),
            data_publicacao=row.dtPub,
            editora=None
        )

    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    def criar(self, livro: Livro) -> bool:
        """
        Inserts a Livro into the database.
        """

        cursor = self.cursor()

        if cursor is None:
            raise ConnectionError("Database connection is not available.")

        sql = """
            INSERT INTO Livro (
                ISBN,
                Titulo,
                Idioma,
                Tipo,
                Tema,
                dtPub,
                editora
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        try:
            cursor.execute(
                sql,
                livro.ISBN,
                livro.Titulo,
                livro.Idioma,
                self._list_to_db(livro.Tipo),
                self._list_to_db(livro.Tema),
                livro.Data_Publicacao,
                self._editora_id(livro.Editora)
            )

            connection = self.connect()
            if connection is None:
                raise ConnectionError("Database connection is not available.")
            connection.commit()
            return True

        except Exception as e:
            connection = self.connect()
            if connection is not None:
                connection.rollback()
            raise e

    # ---------------------------------------------------------
    # READ - one by ISBN
    # ---------------------------------------------------------

    def obter_por_isbn(self, ISBN: str) -> Optional[Livro]:
        """
        Gets one Livro by ISBN.
        Returns None if not found.
        """

        cursor = self.cursor()

        if cursor is None:
            raise ConnectionError("Database connection is not available.")

        sql = """
            SELECT
                ISBN,
                Titulo,
                Idioma,
                Tipo,
                Tema,
                dtPub,
                editora
            FROM Livro
            WHERE ISBN = ?
        """

        cursor.execute(sql, ISBN)
        row = cursor.fetchone()

        if row is None:
            return None

        return self._row_to_livro(row)

    # ---------------------------------------------------------
    # READ - list all / filtered
    # ---------------------------------------------------------

    def listar(
        self,
        filtros: dict | None = None,
        order_by: str = "titulo",
        direction: str = "ascendente"
    ) -> list[Livro]:
        """
        Lists Livro records.

        Supported filters:
        - ISBN
        - titulo
        - idioma
        - ano_publicacao

        Supported order_by:
        - ISBN
        - titulo
        """

        filtros = filtros or {}

        allowed_order = {
            "isbn": "ISBN",
            "titulo": "Titulo"
        }

        allowed_direction = {
            "asc": "ASC",
            "ascendente": "ASC",
            "desc": "DESC",
            "descendente": "DESC"
        }

        order_column = allowed_order.get(order_by.lower(), "Titulo")
        sql_direction = allowed_direction.get(direction.lower(), "ASC")

        sql = """
            SELECT
                ISBN,
                Titulo,
                Idioma,
                Tipo,
                Tema,
                dtPub,
                editora
            FROM Livro
            WHERE 1 = 1
        """

        params = []

        if "ISBN" in filtros:
            sql += " AND ISBN = ?"
            params.append(filtros["ISBN"])

        if "titulo" in filtros:
            sql += " AND Titulo LIKE ?"
            params.append(f"%{filtros['titulo']}%")

        sql += f" ORDER BY {order_column} {sql_direction}"

        cursor = self.cursor()

        if cursor is None:
            raise ConnectionError("Database connection is not available.")

        cursor.execute(sql, params)
        rows = cursor.fetchall()

        return [self._row_to_livro(row) for row in rows]

    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------

    def atualizar(self, livro: Livro) -> bool:
        """
        Updates a Livro in the database using its ISBN.
        """

        cursor = self.cursor()

        if cursor is None:
            raise ConnectionError("Database connection is not available.")

        sql = """
            UPDATE Livro
            SET
                Titulo = ?,
                Idioma = ?,
                Tipo = ?,
                Tema = ?,
                dtPub = ?,
                editora = ?
            WHERE ISBN = ?
        """

        try:
            cursor.execute(
                sql,
                livro.Titulo,
                livro.Idioma,
                self._list_to_db(livro.Tipo),
                self._list_to_db(livro.Tema),
                livro.Data_Publicacao,
                self._editora_id(livro.Editora),
                livro.ISBN
            )

            connection = self.connect()
            if connection is None:
                raise ConnectionError("Database connection is not available.")
            connection.commit()
            return True

        except Exception as e:
            connection = self.connect()
            if connection is not None:
                connection.rollback()
            raise e

    # ---------------------------------------------------------
    # DELETE
    # ---------------------------------------------------------

    def apagar(self, ISBN: str) -> bool:
        """
        Deletes a Livro by ISBN.
        """

        cursor = self.cursor()

        if cursor is None:
            raise ConnectionError("Database connection is not available.")

        sql = """
            DELETE FROM Livro
            WHERE ISBN = ?
        """

        try:
            cursor.execute(sql, ISBN)
            connection = self.connect()
            if connection is None:
                raise ConnectionError("Database connection is not available.")
            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:
            connection = self.connect()
            if connection is not None:
                connection.rollback()
            raise e

    # ---------------------------------------------------------
    # EXISTS
    # ---------------------------------------------------------

    def existe(self, ISBN: str) -> bool:
        """
        Checks if a Livro exists.
        """

        cursor = self.cursor()

        if cursor is None:
            raise ConnectionError("Database connection is not available.")

        sql = """
            SELECT COUNT(*) AS total
            FROM Livro
            WHERE ISBN = ?
        """

        cursor.execute(sql, ISBN)
        row = cursor.fetchone()

        return row is not None and row.total > 0