# -*- coding: utf-8 -*-
# Proper use requires the installation of the "behave" package (pip install behave) in the development environment 
# (preferably in a virtualenv)
# To run test, execute comand: python -m behave .\bdd

from pathlib import Path
import sys
import unicodedata

from behave import then

# ---------------------------------------------------------
# Import path setup
# ---------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

# Needed because livro_dao.py imports from desktop_app...
for path in (PROJECT_ROOT, SRC_DIR):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)

from src.desktop_app.dao.livro_dao import LivroDAO


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------
def normalize_text(value):
    if value is None:
        return ""

    text = str(value).strip().casefold()
    text = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in text if unicodedata.category(ch) != "Mn")


def publication_year(value):
    if value is None:
        return ""

    if hasattr(value, "year"):
        return value.year

    text = str(value).strip()

    if len(text) >= 4 and text[:4].isdigit():
        return int(text[:4])

    return text


# ---------------------------------------------------------
# Service used by steps
# Adapter between LivroDAO/Livro objects and existing BDD steps
# ---------------------------------------------------------
class CatalogService:
    def __init__(self, dao: LivroDAO):
        self.dao = dao

        self.default_fields = ["titulo", "autor", "idioma", "ano_publicacao"]
        self.default_options = ["consultar_detalhes", "ordenar", "filtrar", "navegar"]

        self.current_page = None
        self.list_loaded = False

        self.order_field = None
        self.order_direction = None

        self.filters = {}
        self.visible_titles = []
        self.last_filter_was_applied = None

    def load_home_page(self):
        self.current_page = "home"
        self.list_loaded = True
        self.rebuild_list()

    def rebuild_list(self):
        livros = self.dao.listar()

        autores_por_isbn = self._load_authors_by_isbn(
            [livro.ISBN for livro in livros]
        )

        rows = [
            self._livro_to_catalog_row(livro, autores_por_isbn)
            for livro in livros
        ]

        rows = self._apply_filters(rows)
        rows = self._apply_order(rows)

        self.visible_titles = rows

    def set_order(self, field, direction):
        allowed_fields = {"titulo", "autor"}
        allowed_directions = {"ascendente", "descendente"}

        if field not in allowed_fields:
            raise ValueError(f"Campo de ordenação inválido: {field}")

        if direction not in allowed_directions:
            raise ValueError(f"Sentido de ordenação inválido: {direction}")

        self.order_field = field
        self.order_direction = direction
        self.rebuild_list()

    def apply_filter(self, field, value):
        if len(value.strip()) < 4:
            self.last_filter_was_applied = False
            return False

        allowed_filters = {"titulo", "autor", "idioma", "ano_publicacao"}

        if field not in allowed_filters:
            raise ValueError(f"Filtro não suportado: {field}")

        self.filters[field] = value
        self.last_filter_was_applied = True
        self.rebuild_list()
        return True

    def navigate_list(self):
        return self.visible_titles

    def current_isbns(self):
        return [row["isbn"] for row in self.visible_titles]

    def _livro_to_catalog_row(self, livro, autores_por_isbn):
        isbn = str(livro.ISBN).strip()

        return {
            "isbn": isbn,
            "titulo": livro.Titulo,
            "autor": autores_por_isbn.get(isbn, "(autor não registado)"),
            "idioma": livro.Idioma,
            "ano_publicacao": publication_year(livro.Data_Publicacao),
            "details_ref": isbn,
        }

    def _apply_filters(self, rows):
        result = rows

        for field, raw_value in self.filters.items():
            expected = normalize_text(raw_value)

            result = [
                row for row in result
                if expected in normalize_text(row.get(field, ""))
            ]

        return result

    def _apply_order(self, rows):
        order_field = self.order_field or "titulo"
        reverse = self.order_direction == "descendente"

        return sorted(
            rows,
            key=lambda row: normalize_text(row.get(order_field, "")),
            reverse=reverse,
        )

    def _load_authors_by_isbn(self, isbns):
        isbns = [str(isbn).strip() for isbn in isbns if isbn]

        if not isbns:
            return {}

        cursor = self.dao.cursor()

        if cursor is None:
            raise RuntimeError("Não foi possível obter cursor da base de dados.")

        placeholders = ", ".join("?" for _ in isbns)

        sql = f"""
            SELECT
                RTRIM(e.livro) AS ISBN,
                STRING_AGG(a.nome, N'; ') WITHIN GROUP (ORDER BY a.nome) AS autores
            FROM escreve e
            INNER JOIN autor a
                ON RTRIM(a.id_pessoa) = RTRIM(e.autor)
            WHERE RTRIM(e.livro) IN ({placeholders})
            GROUP BY RTRIM(e.livro)
        """

        cursor.execute(sql, isbns)
        rows = cursor.fetchall()

        return {
            str(row.ISBN).strip(): row.autores
            for row in rows
        }


# ---------------------------------------------------------
# Missing step in catalog_steps.py
# Kept here to avoid changing files outside environment.py
# ---------------------------------------------------------
@then("esse filtro é aplicado")
def step_then_filtro_aplicado(context):
    assert context.last_action_result is True, "O filtro deveria ter sido aplicado."


# ---------------------------------------------------------
# Behave hooks
# ---------------------------------------------------------
def before_all(context):
    context.dao = LivroDAO()

    if context.dao.connect() is None:
        raise RuntimeError("Não foi possível estabelecer ligação à base de dados.")

    context.catalog_dao = context.dao


def before_scenario(context, scenario):
    context.catalog = CatalogService(context.catalog_dao)

    context.ids_before_last_action = []
    context.ids_after_last_action = []
    context.last_action_result = None