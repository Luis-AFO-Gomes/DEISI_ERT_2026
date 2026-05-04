import pyodbc
import configparser
from pathlib import Path
import platform

class DAO:
    __conn_str: str
    __db_connection: pyodbc.Connection|None

    def __init__(self):
        config = configparser.ConfigParser()
        ini_path = Path(__file__).resolve().parent.parent / "config" / "config.ini"
        print(f"Loading configuration from: {ini_path}")
        config.read(ini_path, encoding="utf-8")
    
        self.__conn_str = (f"DRIVER={{{config['myMSSQLdb']['driver']}}};"
            f"SERVER={config['myMSSQLdb']['host']};"
            f"DATABASE={config['myMSSQLdb']['db']};"
            f"UID={config['myMSSQLdb']['user']};"
            f"PWD={config['myMSSQLdb']['pass']};"   
            f"Encrypt={config['myMSSQLdb']['encrypt']};"
            f"TrustServerCertificate={config['myMSSQLdb']['trust_server_certificate']};"
        )

        print("Connecting to database...")  
#        print(f"Connection string: {self.__conn_str}")
        try:
            self.__db_connection = pyodbc.connect(self.__conn_str)
            print("Connection established successfully.")
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")
            self.__db_connection = None

    def __del__(self):
        if self.__db_connection:
            self.__db_connection.close()
            print("Database connection closed.")

    def __str__(self) -> str:
        return f"DAO(Connection String: {self.__conn_str})"            

    def connect(self) -> pyodbc.Connection|None:
        return self.__db_connection

    def cursor(self) -> pyodbc.Cursor|None:
        if self.__db_connection:
            return self.__db_connection.cursor()
        return None

    def val_env(self):
        print(f"plataform:{platform.architecture()}")
        print(f"drivers: {pyodbc.drivers()}")

        config = configparser.ConfigParser()
        ini_path = Path(__file__).resolve().parent.parent / "config" / "config.ini"
        config.read(ini_path, encoding="utf-8")

        # print("Loaded files:", config)
        print("Sections:", config.sections())

        print(f"driver: {config['myMSSQLdb']['driver']}")

    def listar_titulos(self, filtros=None, order_by=None, direction="ascendente"):
        filtros = dict(filtros or {})

        allowed_filters = {"titulo", "autor", "idioma", "ano_publicacao"}
        order_map = {
            "titulo": "catalogo.titulo",
            "autor": "catalogo.autor",
        }

        sql = """
    WITH catalogo AS (
        SELECT
            RTRIM(l.ISBN) AS ISBN,
            l.titulo AS titulo,
            COALESCE(auth.autores, N'(autor não registado)') AS autor,
            l.idioma AS idioma,
            CAST(l.dtPub AS int) AS ano_publicacao
        FROM biblioteca.dbo.livro l
        OUTER APPLY (
            SELECT STRING_AGG(a.nome, N'; ') WITHIN GROUP (ORDER BY a.nome) AS autores
            FROM biblioteca.dbo.escreve e
            INNER JOIN biblioteca.dbo.autor a
                ON RTRIM(a.id_pessoa) = RTRIM(e.autor)
            WHERE RTRIM(e.livro) = RTRIM(l.ISBN)
        ) auth
    )
    SELECT
        catalogo.ISBN,
        catalogo.titulo,
        catalogo.autor,
        catalogo.idioma,
        catalogo.ano_publicacao
    FROM catalogo
    """

        where_clauses = []
        params = []

        for field, raw_value in filtros.items():
            if field not in allowed_filters:
                raise ValueError(f"Filtro não suportado: {field}")

            if field == "titulo":
                where_clauses.append("catalogo.titulo COLLATE Latin1_General_CI_AI LIKE ?")
                params.append(f"%{raw_value}%")

            elif field == "autor":
                where_clauses.append("catalogo.autor COLLATE Latin1_General_CI_AI LIKE ?")
                params.append(f"%{raw_value}%")

            elif field == "idioma":
                where_clauses.append("catalogo.idioma COLLATE Latin1_General_CI_AI LIKE ?")
                params.append(f"%{raw_value}%")

            elif field == "ano_publicacao":
                where_clauses.append("CAST(catalogo.ano_publicacao AS varchar(4)) LIKE ?")
                params.append(f"%{raw_value}%")

        if where_clauses:
            sql += "\nWHERE " + "\n  AND ".join(where_clauses)

        if order_by:
            if order_by not in order_map:
                raise ValueError(f"Campo de ordenação inválido: {order_by}")

            direction_sql = "ASC" if direction == "ascendente" else "DESC"
            sql += f"\nORDER BY {order_map[order_by]} {direction_sql}"
        else:
            sql += "\nORDER BY catalogo.titulo ASC"

        cursor = self.cursor()
        if cursor is None:
            raise RuntimeError("Não foi possível obter cursor da base de dados.")

        cursor.execute(sql, params)
        rows = cursor.fetchall()

        result = []
        for row in rows:
            result.append({
                "isbn": row.ISBN,
                "titulo": row.titulo,
                "autor": row.autor,
                "idioma": row.idioma,
                "ano_publicacao": row.ano_publicacao,
                "details_ref": row.ISBN,
            })

        return result


