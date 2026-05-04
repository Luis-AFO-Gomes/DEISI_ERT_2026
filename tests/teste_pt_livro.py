import pytest

from src.desktop_app.models.livro import Livro


class FakeEditora:
    def __init__(self, nome="Editora Teste"):
        self.nome = nome

    def get_nome(self):
        return self.nome


@pytest.fixture(autouse=True)
def clear_livro_registry():
    Livro._by_ISBN.clear()
    yield
    Livro._by_ISBN.clear()


def test_constructor_and_properties():
    editora = FakeEditora()

    livro = Livro(
        ISBN="9780000000001",
        Titulo="Livro Teste",
        idioma="Português",
        tipo=["Romance"],
        tema=["História"],
        data_publicacao=2024,
        editora=None        # editora (using None because FakeEditora is not defined in this test, Editora Class is not implemented yet)
    )

    assert livro.ISBN == "9780000000001"
    assert livro.Titulo == "Livro Teste"
    assert livro.Idioma == "Português"
    assert livro.Tipo == ["Romance"]
    assert livro.Tema == ["História"]
    assert livro.Data_Publicacao == 2024
    assert livro.Editora is None


def test_property_setters():
    livro = Livro("1", "A", "PT", [], [], 2020, None)

    livro.ISBN = "2"
    livro.Titulo = "Novo Título"
    livro.Idioma = "EN"
    livro.Tipo = ["Técnico"]
    livro.Tema = ["Python"]
    livro.Data_Publicacao = 2025
    livro.Editora = None

    assert livro.ISBN == "2"
    assert livro.Titulo == "Novo Título"
    assert livro.Idioma == "EN"
    assert livro.Tipo == ["Técnico"]
    assert livro.Tema == ["Python"]
    assert livro.Data_Publicacao == 2025
    assert livro.Editora is None


def test_to_dict():
    editora = FakeEditora()

    livro = Livro(
        "9780000000001",
        "Livro Teste",
        "Português",
        ["Romance"],
        ["História"],
        2024,
        None
    )

    result = livro.to_dict()

    assert result == {
        "ISBN": "9780000000001",
        "Titulo": "Livro Teste",
        "Idioma": "Português",
        "Tipo": ["Romance"],
        "Tema": ["História"],
        "Data_Publicacao": 2024,
        "Editora": None
    }


def test_from_dict():
    editora = FakeEditora()

    data = {
        "ISBN": "9780000000001",
        "Titulo": "Livro Teste",
        "Idioma": "Português",
        "Tipo": ["Romance"],
        "Tema": ["História"],
        "Data_Publicacao": 2024,
        "Editora": editora
    }

    livro = Livro.from_dict(data)

    assert livro.ISBN == "9780000000001"
    assert livro.Titulo == "Livro Teste"
    assert livro.Idioma == "Português"
    assert livro.Tipo == ["Romance"]
    assert livro.Tema == ["História"]
    assert livro.Data_Publicacao == 2024
    assert livro.Editora is editora


def test_create_unique_success():
    livro = Livro._create_unique(
        "9780000000001",
        "Livro Teste",
        "Português",
        ["Romance"],
        ["História"],
        2024,
        None
    )

    assert "9780000000001" in Livro._by_ISBN
    assert Livro._by_ISBN["9780000000001"] is livro


def test_create_unique_duplicate_raises_value_error():
    Livro._create_unique(
        "9780000000001",
        "Livro Teste",
        "Português",
        [],
        [],
        2024,
        None
    )

    with pytest.raises(ValueError):
        Livro._create_unique(
            "9780000000001",
            "Outro Livro",
            "Português",
            [],
            [],
            2025,
            None
        )


def test_adicionar_tipo_adds_new_value():
    livro = Livro("1", "Livro", "PT", [], [], 2020, None)

    livro.adicionar_tipo("Romance")

    assert livro.Tipo == ["Romance"]


def test_adicionar_tipo_does_not_duplicate_value():
    livro = Livro("1", "Livro", "PT", ["Romance"], [], 2020, None)

    livro.adicionar_tipo("Romance")

    assert livro.Tipo == ["Romance"]


def test_adicionar_tema_adds_new_value():
    livro = Livro("1", "Livro", "PT", [], [], 2020, None)

    livro.adicionar_tema("História")

    assert livro.Tema == ["História"]


def test_adicionar_tema_does_not_duplicate_value():
    livro = Livro("1", "Livro", "PT", [], ["História"], 2020, None)

    livro.adicionar_tema("História")

    assert livro.Tema == ["História"]


def test_str_without_editora():
    livro = Livro(
        "9780000000001",
        "Livro Teste",
        "Português",
        [],
        [],
        2024,
        None
    )

    result = str(livro)

    assert "Livro: Livro Teste" in result
    assert "com ISBN: 9780000000001" in result
    assert "editado a 2024" in result
    assert "em Português" in result


def test_str_with_editora():
    livro = Livro(
        "9780000000001",
        "Livro Teste",
        "Português",
        [],
        [],
        2024,
        None
    )

    result = str(livro)

    assert "Livro: Livro Teste" in result
    assert "com ISBN: 9780000000001" in result
    assert "editado a 2024 por Editora XPTO" in result
    assert "em Português" in result


def test_from_input_success(monkeypatch):
    valid_vazio_values = iter([
        "9780000000001",
        "Livro Teste",
        "Português"
    ])

    input_values = iter([
        "Romance",
        "Técnico",
        "",
        "Python",
        "Programação",
        ""
    ])

    monkeypatch.setattr(
        "src.desktop_app.models.livro.val.valid_vazio",
        lambda message: next(valid_vazio_values)
    )

    monkeypatch.setattr(
        "src.desktop_app.models.livro.val.valid_date",
        lambda message: 2024
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda message="": next(input_values)
    )

    livro = Livro.from_input()

    assert livro.ISBN == "9780000000001"
    assert livro.Titulo == "Livro Teste"
    assert livro.Idioma == "Português"
    assert livro.Tipo == ["Romance", "Técnico"]
    assert livro.Tema == ["Python", "Programação"]
    assert livro.Data_Publicacao == 2024
    assert livro.Editora is None
    assert "9780000000001" in Livro._by_ISBN


def test_from_input_duplicate_isbn_raises_value_error(monkeypatch):
    Livro._create_unique(
        "9780000000001",
        "Livro Existente",
        "Português",
        [],
        [],
        2020,
        None
    )

    monkeypatch.setattr(
        "src.desktop_app.models.livro.val.valid_vazio",
        lambda message: "9780000000001"
    )

    with pytest.raises(ValueError):
        Livro.from_input()