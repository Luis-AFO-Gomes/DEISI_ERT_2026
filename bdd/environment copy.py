# -*- coding: utf-8 -*-
# Proper use requires the installation of the "behave" package (pip install behave) in the development environment 
# (preferably in a virtualenv)
# To run test, execute comand: python -m behave .\bdd
from pathlib import Path
import sys

# ---------------------------------------------------------
# Import path setup
# Required to allow importing the DAO class from the parent directory (project root)
# ---------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.desktop_app.dao.database import DAO
from src.desktop_app.models import livro
from src.desktop_app.dao import database



# ---------------------------------------------------------
# Service used by steps
# ---------------------------------------------------------
class CatalogService:
    def __init__(self, dao):
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
        self.visible_titles = self.dao.listar_titulos(
            filtros=self.filters,
            order_by=self.order_field,
            direction=self.order_direction or "ascendente",
        )

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

        self.filters[field] = value
        self.last_filter_was_applied = True
        self.rebuild_list()
        return True

    def navigate_list(self):
        return self.visible_titles

    def current_isbns(self):
        return [row["isbn"] for row in self.visible_titles]


# ---------------------------------------------------------
# Behave hooks
# Basic functionality to set up the context for the tests, 
# including database connection and service initialization.
# ---------------------------------------------------------
def before_all(context):
    context.dao = DAO()

    if context.dao.connect() is None:
        raise RuntimeError("Não foi possível estabelecer ligação à base de dados.")

    context.catalog_dao = context.dao


def before_scenario(context, scenario):
    context.catalog = CatalogService(context.catalog_dao)

    context.ids_before_last_action = []
    context.ids_after_last_action = []
    context.last_action_result = None