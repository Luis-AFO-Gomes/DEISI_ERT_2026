import unittest
from unittest.mock import patch

from src.desktop_app.models.livro import Livro


class FakeEditora:
    def __init__(self, nome="Editora Teste"):
        self.nome = nome

    def get_nome(self):
        return self.nome


class TestLivro(unittest.TestCase):

    def setUp(self):
        Livro._by_ISBN.clear()

    def test_constructor_and_properties(self):
        editora = FakeEditora()

        livro = Livro(
            ISBN="9780000000001",
            Titulo="Livro Teste",
            idioma="Português",
            tipo=["Romance"],
            tema=["História"],
            data_publicacao=2024,
            editora=None
        )

        self.assertEqual(livro.ISBN, "9780000000001")
        self.assertEqual(livro.Titulo, "Livro Teste")
        self.assertEqual(livro.Idioma, "Português")
        self.assertEqual(livro.Tipo, ["Romance"])
        self.assertEqual(livro.Tema, ["História"])
        self.assertEqual(livro.Data_Publicacao, 2024)
        self.assertIs(livro.Editora, editora)

    def test_property_setters(self):
        livro = Livro("1", "A", "PT", [], [], 2020, None)

        livro.ISBN = "2"
        livro.Titulo = "Novo Título"
        livro.Idioma = "EN"
        livro.Tipo = ["Técnico"]
        livro.Tema = ["Python"]
        livro.Data_Publicacao = 2025
        livro.Editora = FakeEditora("Nova Editora")

        self.assertEqual(livro.ISBN, "2")
        self.assertEqual(livro.Titulo, "Novo Título")
        self.assertEqual(livro.Idioma, "EN")
        self.assertEqual(livro.Tipo, ["Técnico"])
        self.assertEqual(livro.Tema, ["Python"])
        self.assertEqual(livro.Data_Publicacao, 2025)
        self.assertEqual(livro.Editora.get_nome(), "Nova Editora")

    def test_to_dict(self):
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

        expected = {
            "ISBN": "9780000000001",
            "Titulo": "Livro Teste",
            "Idioma": "Português",
            "Tipo": ["Romance"],
            "Tema": ["História"],
            "Data_Publicacao": 2024,
            "Editora": editora
        }

        self.assertEqual(result, expected)

    def test_from_dict(self):
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

        self.assertEqual(livro.ISBN, "9780000000001")
        self.assertEqual(livro.Titulo, "Livro Teste")
        self.assertEqual(livro.Idioma, "Português")
        self.assertEqual(livro.Tipo, ["Romance"])
        self.assertEqual(livro.Tema, ["História"])
        self.assertEqual(livro.Data_Publicacao, 2024)
        self.assertIs(livro.Editora, editora)

    def test_create_unique_success(self):
        livro = Livro._create_unique(
            "9780000000001",
            "Livro Teste",
            "Português",
            ["Romance"],
            ["História"],
            2024,
            None
        )

        self.assertIn("9780000000001", Livro._by_ISBN)
        self.assertIs(Livro._by_ISBN["9780000000001"], livro)

    def test_create_unique_duplicate_raises_value_error(self):
        Livro._create_unique(
            "9780000000001",
            "Livro Teste",
            "Português",
            [],
            [],
            2024,
            None
        )

        with self.assertRaises(ValueError):
            Livro._create_unique(
                "9780000000001",
                "Outro Livro",
                "Português",
                [],
                [],
                2025,
                None
            )

    def test_adicionar_tipo_adds_new_value(self):
        livro = Livro("1", "Livro", "PT", [], [], 2020, None)

        livro.adicionar_tipo("Romance")

        self.assertEqual(livro.Tipo, ["Romance"])

    def test_adicionar_tipo_does_not_duplicate_value(self):
        livro = Livro("1", "Livro", "PT", ["Romance"], [], 2020, None)

        livro.adicionar_tipo("Romance")

        self.assertEqual(livro.Tipo, ["Romance"])

    def test_adicionar_tema_adds_new_value(self):
        livro = Livro("1", "Livro", "PT", [], [], 2020, None)

        livro.adicionar_tema("História")

        self.assertEqual(livro.Tema, ["História"])

    def test_adicionar_tema_does_not_duplicate_value(self):
        livro = Livro("1", "Livro", "PT", [], ["História"], 2020, None)

        livro.adicionar_tema("História")

        self.assertEqual(livro.Tema, ["História"])

    def test_str_without_editora(self):
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

        self.assertIn("Livro: Livro Teste", result)
        self.assertIn("com ISBN: 9780000000001", result)
        self.assertIn("editado a 2024", result)
        self.assertIn("em Português", result)

    def test_str_with_editora(self):
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

        self.assertIn("Livro: Livro Teste", result)
        self.assertIn("com ISBN: 9780000000001", result)
        self.assertIn("editado a 2024", result)
        self.assertIn("em Português", result)

    @patch("builtins.input")
    @patch("src.desktop_app.models.livro.val.valid_date")
    @patch("src.desktop_app.models.livro.val.valid_vazio")
    def test_from_input_success(self, mock_valid_vazio, mock_valid_date, mock_input):
        mock_valid_vazio.side_effect = [
            "9780000000001",
            "Livro Teste",
            "Português"
        ]

        mock_input.side_effect = [
            "Romance",
            "Técnico",
            "",
            "Python",
            "Programação",
            ""
        ]

        mock_valid_date.return_value = 2024

        livro = Livro.from_input()

        self.assertEqual(livro.ISBN, "9780000000001")
        self.assertEqual(livro.Titulo, "Livro Teste")
        self.assertEqual(livro.Idioma, "Português")
        self.assertEqual(livro.Tipo, ["Romance", "Técnico"])
        self.assertEqual(livro.Tema, ["Python", "Programação"])
        self.assertEqual(livro.Data_Publicacao, 2024)
        self.assertIsNone(livro.Editora)

        self.assertIn("9780000000001", Livro._by_ISBN)

    @patch("src.desktop_app.models.livro.val.valid_vazio")
    def test_from_input_duplicate_isbn_raises_value_error(self, mock_valid_vazio):
        Livro._create_unique(
            "9780000000001",
            "Livro Existente",
            "Português",
            [],
            [],
            2020,
            None
        )

        mock_valid_vazio.return_value = "9780000000001"

        with self.assertRaises(ValueError):
            Livro.from_input()


if __name__ == "__main__":
    unittest.main()