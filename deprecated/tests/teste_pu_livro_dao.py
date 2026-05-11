import unittest
import json
from types import SimpleNamespace
from unittest.mock import MagicMock

from src.desktop_app.dao.livro_dao import LivroDAO
from src.desktop_app.models.livro import Livro


class FakeConnection:
    def __init__(self):
        self.commit = MagicMock()
        self.rollback = MagicMock()


class FakeCursor:
    def __init__(self):
        self.execute = MagicMock()
        self.fetchone = MagicMock()
        self.fetchall = MagicMock()
        self.rowcount = 0


class FakeEditora:
    def __init__(self, id_value):
        self.id_value = id_value

    def get_id(self):
        return self.id_value


class TestLivroDAOHelpers(unittest.TestCase):

    def test_list_to_db_with_list(self):
        result = LivroDAO._list_to_db(["Romance", "Técnico"])

        self.assertEqual(
            result,
            json.dumps(["Romance", "Técnico"], ensure_ascii=False)
        )

    def test_list_to_db_with_none_returns_empty_json_list(self):
        result = LivroDAO._list_to_db(None)

        self.assertEqual(result, "[]")

    def test_list_from_db_with_valid_json_list(self):
        result = LivroDAO._list_from_db('["Romance", "Técnico"]')

        self.assertEqual(result, ["Romance", "Técnico"])

    def test_list_from_db_with_empty_value_returns_empty_list(self):
        self.assertEqual(LivroDAO._list_from_db(None), [])
        self.assertEqual(LivroDAO._list_from_db(""), [])

    def test_list_from_db_with_invalid_json_returns_empty_list(self):
        result = LivroDAO._list_from_db("texto inválido")

        self.assertEqual(result, [])

    def test_list_from_db_with_json_scalar_returns_single_item_list(self):
        result = LivroDAO._list_from_db('"Romance"')

        self.assertEqual(result, ["Romance"])

    def test_editora_id_with_none(self):
        result = LivroDAO._editora_id(None)

        self.assertIsNone(result)

    def test_editora_id_with_get_id(self):
        editora = FakeEditora("EDITORA001")

        result = LivroDAO._editora_id(None)

        self.assertEqual(result, "EDITORA001")

    def test_row_to_livro(self):
        row = SimpleNamespace(
            ISBN="9780000000001",
            Titulo="Livro Teste",
            Idioma="Português",
            Tipo='["Romance"]',
            Tema='["História"]',
            dtPub=2024,
            editora="EDITORA001"
        )

        livro = LivroDAO._row_to_livro(row)

        self.assertIsInstance(livro, Livro)
        self.assertEqual(livro.ISBN, "9780000000001")
        self.assertEqual(livro.Titulo, "Livro Teste")
        self.assertEqual(livro.Idioma, "Português")
        self.assertEqual(livro.Tipo, ["Romance"])
        self.assertEqual(livro.Tema, ["História"])
        self.assertEqual(livro.Data_Publicacao, 2024)
        self.assertIsNone(livro.Editora)


class TestLivroDAOCRUD(unittest.TestCase):

    def setUp(self):
        self.dao = LivroDAO.__new__(LivroDAO)

        self.cursor = FakeCursor()
        self.connection = FakeConnection()

        self.dao.cursor = MagicMock(return_value=self.cursor)
        self.dao.connect = MagicMock(return_value=self.connection)

        self.livro = Livro(
            ISBN="9780000000001",
            Titulo="Livro Teste",
            idioma="Português",
            tipo=["Romance"],
            tema=["História"],
            data_publicacao=2024,
            editora=None,
            disponivel="disponivel"
        )

    def test_criar_success(self):
        result = self.dao.criar(self.livro)

        self.assertTrue(result)

        self.cursor.execute.assert_called_once()
        sql, *params = self.cursor.execute.call_args.args

        self.assertIn("INSERT INTO Livro", sql)
        self.assertEqual(params[0], "9780000000001")
        self.assertEqual(params[1], "Livro Teste")
        self.assertEqual(params[2], "Português")
        self.assertEqual(params[3], '["Romance"]')
        self.assertEqual(params[4], '["História"]')
        self.assertEqual(params[5], 2024)
        self.assertIsNone(params[6])

        self.connection.commit.assert_called_once()
        self.connection.rollback.assert_not_called()

    def test_criar_without_cursor_raises_connection_error(self):
        self.dao.cursor = MagicMock(return_value=None)

        with self.assertRaises(ConnectionError):
            self.dao.criar(self.livro)

    def test_criar_execute_error_rolls_back(self):
        self.cursor.execute.side_effect = Exception("Erro SQL")

        with self.assertRaises(Exception):
            self.dao.criar(self.livro)

        self.connection.rollback.assert_called_once()
        self.connection.commit.assert_not_called()

    def test_obter_por_isbn_found(self):
        self.cursor.fetchone.return_value = SimpleNamespace(
            ISBN="9780000000001",
            Titulo="Livro Teste",
            Idioma="Português",
            Tipo='["Romance"]',
            Tema='["História"]',
            dtPub=2024,
            editora=None,
            disponivel="disponivel"
        )

        livro = self.dao.obter_por_isbn("9780000000001")

        self.assertIsInstance(livro, Livro)
        assert livro is not None
        self.assertEqual(livro.ISBN, "9780000000001")
        self.assertEqual(livro.Titulo, "Livro Teste")
        self.assertEqual(livro.Idioma, "Português")
        self.assertEqual(livro.Tipo, ["Romance"])
        self.assertEqual(livro.Tema, ["História"])
        self.assertEqual(livro.Data_Publicacao, 2024)

        self.cursor.execute.assert_called_once()
        sql, isbn = self.cursor.execute.call_args.args

        self.assertIn("SELECT", sql)
        self.assertIn("FROM Livro", sql)
        self.assertIn("WHERE ISBN = ?", sql)
        self.assertEqual(isbn, "9780000000001")

    def test_obter_por_isbn_not_found_returns_none(self):
        self.cursor.fetchone.return_value = None

        result = self.dao.obter_por_isbn("9780000000001")

        self.assertIsNone(result)

    def test_obter_por_isbn_without_cursor_raises_connection_error(self):
        self.dao.cursor = MagicMock(return_value=None)

        with self.assertRaises(ConnectionError):
            self.dao.obter_por_isbn("9780000000001")

    def test_listar_without_filters_orders_by_titulo_ascending(self):
        self.cursor.fetchall.return_value = [
            SimpleNamespace(
                ISBN="9780000000001",
                Titulo="Livro A",
                Idioma="Português",
                Tipo='["Romance"]',
                Tema='["História"]',
                dtPub=2024,
                editora=None
            ),
            SimpleNamespace(
                ISBN="9780000000002",
                Titulo="Livro B",
                Idioma="Inglês",
                Tipo='["Técnico"]',
                Tema='["Python"]',
                dtPub=2023,
                editora=None
            )
        ]

        result = self.dao.listar()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].Titulo, "Livro A")
        self.assertEqual(result[1].Titulo, "Livro B")

        self.cursor.execute.assert_called_once()
        sql, params = self.cursor.execute.call_args.args

        self.assertIn("FROM Livro", sql)
        self.assertIn("WHERE 1 = 1", sql)
        self.assertIn("ORDER BY Titulo ASC", sql)
        self.assertEqual(params, [])

    def test_listar_with_filters(self):
        self.cursor.fetchall.return_value = []

        filtros = {
            "ISBN": "9780000000001",
            "titulo": "Python",
            "disponivel": "disponivel"
        }

        result = self.dao.listar(
            filtros=filtros,
            order_by="isbn",
            direction="descendente"
        )

        self.assertEqual(result, [])

        self.cursor.execute.assert_called_once()
        sql, params = self.cursor.execute.call_args.args

        self.assertIn("AND ISBN = ?", sql)
        self.assertIn("AND Titulo LIKE ?", sql)
        self.assertIn("AND disponivel = ?", sql)
        self.assertIn("ORDER BY ISBN DESC", sql)

        self.assertEqual(
            params,
            [
                "9780000000001",
                "%Python%",
                1
            ]
        )

    def test_listar_with_invalid_order_and_direction_uses_defaults(self):
        self.cursor.fetchall.return_value = []

        self.dao.listar(order_by="campo_invalido", direction="sentido_invalido")

        sql, params = self.cursor.execute.call_args.args

        self.assertIn("ORDER BY Titulo ASC", sql)
        self.assertEqual(params, [])

    def test_listar_without_cursor_raises_connection_error(self):
        self.dao.cursor = MagicMock(return_value=None)

        with self.assertRaises(ConnectionError):
            self.dao.listar()

    def test_atualizar_success(self):
        result = self.dao.atualizar(self.livro)

        self.assertTrue(result)

        self.cursor.execute.assert_called_once()
        sql, *params = self.cursor.execute.call_args.args

        self.assertIn("UPDATE Livro", sql)
        self.assertIn("WHERE ISBN = ?", sql)

        self.assertEqual(params[0], "Livro Teste")
        self.assertEqual(params[1], "Português")
        self.assertEqual(params[2], '["Romance"]')
        self.assertEqual(params[3], '["História"]')
        self.assertEqual(params[4], 2024)
        self.assertIsNone(params[5])
        self.assertEqual(params[6], "9780000000001")

        self.connection.commit.assert_called_once()
        self.connection.rollback.assert_not_called()

    def test_atualizar_without_cursor_raises_connection_error(self):
        self.dao.cursor = MagicMock(return_value=None)

        with self.assertRaises(ConnectionError):
            self.dao.atualizar(self.livro)

    def test_atualizar_execute_error_rolls_back(self):
        self.cursor.execute.side_effect = Exception("Erro SQL")

        with self.assertRaises(Exception):
            self.dao.atualizar(self.livro)

        self.connection.rollback.assert_called_once()
        self.connection.commit.assert_not_called()

    def test_apagar_success_existing_row(self):
        self.cursor.rowcount = 1

        result = self.dao.apagar("9780000000001")

        self.assertTrue(result)

        self.cursor.execute.assert_called_once()
        sql, isbn = self.cursor.execute.call_args.args

        self.assertIn("DELETE FROM Livro", sql)
        self.assertIn("WHERE ISBN = ?", sql)
        self.assertEqual(isbn, "9780000000001")

        self.connection.commit.assert_called_once()
        self.connection.rollback.assert_not_called()

    def test_apagar_success_no_row_deleted(self):
        self.cursor.rowcount = 0

        result = self.dao.apagar("9780000000001")

        self.assertFalse(result)

        self.connection.commit.assert_called_once()
        self.connection.rollback.assert_not_called()

    def test_apagar_without_cursor_raises_connection_error(self):
        self.dao.cursor = MagicMock(return_value=None)

        with self.assertRaises(ConnectionError):
            self.dao.apagar("9780000000001")

    def test_apagar_execute_error_rolls_back(self):
        self.cursor.execute.side_effect = Exception("Erro SQL")

        with self.assertRaises(Exception):
            self.dao.apagar("9780000000001")

        self.connection.rollback.assert_called_once()
        self.connection.commit.assert_not_called()

    def test_existe_true(self):
        self.cursor.fetchone.return_value = SimpleNamespace(total=1)

        result = self.dao.existe("9780000000001")

        self.assertTrue(result)

        self.cursor.execute.assert_called_once()
        sql, isbn = self.cursor.execute.call_args.args

        self.assertIn("SELECT COUNT(*) AS total", sql)
        self.assertIn("FROM Livro", sql)
        self.assertIn("WHERE ISBN = ?", sql)
        self.assertEqual(isbn, "9780000000001")

    def test_existe_false_when_total_zero(self):
        self.cursor.fetchone.return_value = SimpleNamespace(total=0)

        result = self.dao.existe("9780000000001")

        self.assertFalse(result)

    def test_existe_false_when_no_row(self):
        self.cursor.fetchone.return_value = None

        result = self.dao.existe("9780000000001")

        self.assertFalse(result)

    def test_existe_without_cursor_raises_connection_error(self):
        self.dao.cursor = MagicMock(return_value=None)

        with self.assertRaises(ConnectionError):
            self.dao.existe("9780000000001")


if __name__ == "__main__":
    unittest.main()