import json
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

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


@pytest.fixture
def dao_with_mocks():
    dao = LivroDAO.__new__(LivroDAO)

    cursor = FakeCursor()
    connection = FakeConnection()

    dao.cursor = MagicMock(return_value=cursor)
    dao.connect = MagicMock(return_value=connection)

    return dao, cursor, connection


@pytest.fixture
def livro():
    return Livro(
        ISBN="9780000000001",
        Titulo="Livro Teste",
        idioma="Português",
        tipo=["Romance"],
        tema=["História"],
        data_publicacao=2024,
        editora=None,
        disponivel="disponivel"
    )


def test_list_to_db_with_list():
    result = LivroDAO._list_to_db(["Romance", "Técnico"])

    assert result == json.dumps(["Romance", "Técnico"], ensure_ascii=False)


def test_list_to_db_with_none_returns_empty_json_list():
    result = LivroDAO._list_to_db(None)

    assert result == "[]"


def test_list_from_db_with_valid_json_list():
    result = LivroDAO._list_from_db('["Romance", "Técnico"]')

    assert result == ["Romance", "Técnico"]


def test_list_from_db_with_empty_value_returns_empty_list():
    assert LivroDAO._list_from_db(None) == []
    assert LivroDAO._list_from_db("") == []


def test_list_from_db_with_invalid_json_returns_empty_list():
    result = LivroDAO._list_from_db("texto inválido")

    assert result == []


def test_list_from_db_with_json_scalar_returns_single_item_list():
    result = LivroDAO._list_from_db('"Romance"')

    assert result == ["Romance"]


def test_editora_id_with_none():
    result = LivroDAO._editora_id(None)

    assert result is None


def test_editora_id_with_get_id():
    editora = FakeEditora("EDITORA001")

    result = LivroDAO._editora_id(editora)

    assert result == "EDITORA001"


def test_row_to_livro():
    row = SimpleNamespace(
        ISBN="9780000000001",
        Titulo="Livro Teste",
        Idioma="Português",
        Tipo='["Romance"]',
        Tema='["História"]',
        dtPub=2024,
        editora="EDITORA001",
        disponivel="retirado"
    )

    livro = LivroDAO._row_to_livro(row)

    assert livro.ISBN == "9780000000001"
    assert livro.ISBN == "9780000000001"
    assert livro.Titulo == "Livro Teste"
    assert livro.Idioma == "Português"
    assert livro.Tipo == ["Romance"]
    assert livro.Tema == ["História"]
    assert livro.Data_Publicacao == 2024
    assert livro.Editora is None
    assert livro.Disponivel == "retirado"


def test_criar_success(dao_with_mocks, livro):
    dao, cursor, connection = dao_with_mocks

    result = dao.criar(livro)

    assert result is True

    cursor.execute.assert_called_once()
    sql, *params = cursor.execute.call_args.args

    assert "INSERT INTO Livro" in sql
    assert params[0] == "9780000000001"
    assert params[1] == "Livro Teste"
    assert params[2] == "Português"
    assert params[3] == '["Romance"]'
    assert params[4] == '["História"]'
    assert params[5] == 2024
    assert params[6] is None
    assert params[7] == "disponivel"

    connection.commit.assert_called_once()
    connection.rollback.assert_not_called()


def test_criar_without_cursor_raises_connection_error(dao_with_mocks, livro):
    dao, cursor, connection = dao_with_mocks
    dao.cursor = MagicMock(return_value=None)

    with pytest.raises(ConnectionError):
        dao.criar(livro)


def test_criar_execute_error_rolls_back(dao_with_mocks, livro):
    dao, cursor, connection = dao_with_mocks
    cursor.execute.side_effect = Exception("Erro SQL")

    with pytest.raises(Exception):
        dao.criar(livro)

    connection.rollback.assert_called_once()
    connection.commit.assert_not_called()


def test_obter_por_isbn_found(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks

    cursor.fetchone.return_value = SimpleNamespace(
        ISBN="9780000000001",
        Titulo="Livro Teste",
        Idioma="Português",
        Tipo='["Romance"]',
        Tema='["História"]',
        dtPub=2024,
        editora=None,
        disponivel="disponivel"
    )

    livro = dao.obter_por_isbn("9780000000001")

    assert livro.ISBN == "9780000000001"
    assert livro.ISBN == "9780000000001"
    assert livro.Titulo == "Livro Teste"
    assert livro.Idioma == "Português"
    assert livro.Tipo == ["Romance"]
    assert livro.Tema == ["História"]
    assert livro.Data_Publicacao == 2024
    assert livro.Disponivel == "disponivel"

    cursor.execute.assert_called_once()
    sql, isbn = cursor.execute.call_args.args

    assert "SELECT" in sql
    assert "FROM Livro" in sql
    assert "WHERE ISBN = ?" in sql
    assert isbn == "9780000000001"


def test_obter_por_isbn_not_found_returns_none(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks
    cursor.fetchone.return_value = None

    result = dao.obter_por_isbn("9780000000001")

    assert result is None


def test_obter_por_isbn_without_cursor_raises_connection_error(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks
    dao.cursor = MagicMock(return_value=None)

    with pytest.raises(ConnectionError):
        dao.obter_por_isbn("9780000000001")


def test_listar_without_filters_orders_by_titulo_ascending(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks

    cursor.fetchall.return_value = [
        SimpleNamespace(
            ISBN="9780000000001",
            Titulo="Livro A",
            Idioma="Português",
            Tipo='["Romance"]',
            Tema='["História"]',
            dtPub=2024,
            editora=None,
            disponivel="disponivel"
        ),
        SimpleNamespace(
            ISBN="9780000000002",
            Titulo="Livro B",
            Idioma="Inglês",
            Tipo='["Técnico"]',
            Tema='["Python"]',
            dtPub=2023,
            editora=None,
            disponivel="disponivel"
        )
    ]

    result = dao.listar()

    assert len(result) == 2
    assert result[0].Titulo == "Livro A"
    assert result[1].Titulo == "Livro B"

    cursor.execute.assert_called_once()
    sql, params = cursor.execute.call_args.args

    assert "FROM Livro" in sql
    assert "WHERE 1 = 1" in sql
    assert "ORDER BY Titulo ASC" in sql
    assert params == []


def test_listar_with_filters(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks
    cursor.fetchall.return_value = []

    filtros = {
        "ISBN": "9780000000001",
        "titulo": "Python",
        "disponivel": "disponivel"
    }

    result = dao.listar(
        filtros=filtros,
        order_by="isbn",
        direction="descendente"
    )

    assert result == []

    cursor.execute.assert_called_once()
    sql, params = cursor.execute.call_args.args

    assert "AND ISBN = ?" in sql
    assert "AND Titulo LIKE ?" in sql
    assert "AND disponivel = ?" in sql
    assert "ORDER BY ISBN DESC" in sql

    assert params == [
        "9780000000001",
        "%Python%",
        "disponivel"
    ]


def test_listar_with_invalid_order_and_direction_uses_defaults(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks
    cursor.fetchall.return_value = []

    dao.listar(order_by="campo_invalido", direction="sentido_invalido")

    sql, params = cursor.execute.call_args.args

    assert "ORDER BY Titulo ASC" in sql
    assert params == []


def test_listar_without_cursor_raises_connection_error(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks
    dao.cursor = MagicMock(return_value=None)

    with pytest.raises(ConnectionError):
        dao.listar()


def test_atualizar_success(dao_with_mocks, livro):
    dao, cursor, connection = dao_with_mocks

    result = dao.atualizar(livro)

    assert result is True

    cursor.execute.assert_called_once()
    sql, *params = cursor.execute.call_args.args

    assert "UPDATE Livro" in sql
    assert "WHERE ISBN = ?" in sql

    assert params[0] == "Livro Teste"
    assert params[1] == "Português"
    assert params[2] == '["Romance"]'
    assert params[3] == '["História"]'
    assert params[4] == 2024
    assert params[5] is None
    assert params[6] == "disponivel"
    assert params[7] == "9780000000001"

    connection.commit.assert_called_once()
    connection.rollback.assert_not_called()


def test_atualizar_without_cursor_raises_connection_error(dao_with_mocks, livro):
    dao, cursor, connection = dao_with_mocks
    dao.cursor = MagicMock(return_value=None)

    with pytest.raises(ConnectionError):
        dao.atualizar(livro)


def test_atualizar_execute_error_rolls_back(dao_with_mocks, livro):
    dao, cursor, connection = dao_with_mocks
    cursor.execute.side_effect = Exception("Erro SQL")

    with pytest.raises(Exception):
        dao.atualizar(livro)

    connection.rollback.assert_called_once()
    connection.commit.assert_not_called()


def test_apagar_success_existing_row(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks
    cursor.rowcount = 1

    result = dao.apagar("9780000000001")

    assert result is True

    cursor.execute.assert_called_once()
    sql, isbn = cursor.execute.call_args.args

    assert "DELETE FROM Livro" in sql
    assert "WHERE ISBN = ?" in sql
    assert isbn == "9780000000001"

    connection.commit.assert_called_once()
    connection.rollback.assert_not_called()


def test_apagar_success_no_row_deleted(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks
    cursor.rowcount = 0

    result = dao.apagar("9780000000001")

    assert result is False

    connection.commit.assert_called_once()
    connection.rollback.assert_not_called()


def test_apagar_without_cursor_raises_connection_error(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks
    dao.cursor = MagicMock(return_value=None)

    with pytest.raises(ConnectionError):
        dao.apagar("9780000000001")


def test_apagar_execute_error_rolls_back(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks
    cursor.execute.side_effect = Exception("Erro SQL")

    with pytest.raises(Exception):
        dao.apagar("9780000000001")

    connection.rollback.assert_called_once()
    connection.commit.assert_not_called()


def test_existe_true(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks
    cursor.fetchone.return_value = SimpleNamespace(total=1)

    result = dao.existe("9780000000001")

    assert result is True

    cursor.execute.assert_called_once()
    sql, isbn = cursor.execute.call_args.args

    assert "SELECT COUNT(*) AS total" in sql
    assert "FROM Livro" in sql
    assert "WHERE ISBN = ?" in sql
    assert isbn == "9780000000001"


def test_existe_false_when_total_zero(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks
    cursor.fetchone.return_value = SimpleNamespace(total=0)

    result = dao.existe("9780000000001")

    assert result is False


def test_existe_false_when_no_row(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks
    cursor.fetchone.return_value = None

    result = dao.existe("9780000000001")

    assert result is False


def test_existe_without_cursor_raises_connection_error(dao_with_mocks):
    dao, cursor, connection = dao_with_mocks
    dao.cursor = MagicMock(return_value=None)

    with pytest.raises(ConnectionError):
        dao.existe("9780000000001")
