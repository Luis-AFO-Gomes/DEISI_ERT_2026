# -*- coding: utf-8 -*-
# Proper use requires the installation of the "behave" package (pip install behave) in the development environment 
# (preferably in a virtualenv)
from behave import given, when, then
import unicodedata

# Set text to utf-8 and remove accents for more robust comparisons
def normalize_text(value):
    if value is None:
        return ""
    text = str(value).strip().casefold()
    text = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in text if unicodedata.category(ch) != "Mn")

def assert_all_titles_have_fields(titles, fields):
    assert titles, "A lista visível está vazia."
    for title in titles:
        for field in fields:
            assert field in title, f"Campo em falta no título {title.get('isbn')}: {field}"

def assert_all_titles_have_details_ref(titles):
    assert titles, "A lista visível está vazia."
    for title in titles:
        assert title.get("details_ref"), f"Título sem referência para detalhe: {title}"

def is_unavailable(value):
    """
    Treat anything different from 'disponivel' as not available for loan.
    Examples: 'emprestado', 'retirado', etc.
    """
    return normalize_text(value) != "disponivel"        

# ------------------------------------------------------------------
# REQ-001 - Lista de títulos
# ------------------------------------------------------------------

@given("existem títulos em catálogo")
def step_given_existem_titulos_em_catalogo(context):
    context.catalog.load_home_page()
    assert len(context.catalog.visible_titles) > 0, "Não existem títulos em catálogo."


@given("o utilizador encontra-se na página inicial")
def step_given_utilizador_na_pagina_inicial(context):
    context.catalog.current_page = "home"


@when("a página inicial é carregada")
def step_when_pagina_inicial_carregada(context):
    context.catalog.load_home_page()


@then("o sistema apresenta todos os títulos em catálogo")
def step_then_apresenta_todos_os_titulos(context):
    visible = context.catalog.visible_titles
    assert visible, "Nenhum título foi apresentado."

    # All books in the test database should be visible
    # Adjust len (currently set to 8) based on the provided SQL data
    isbns = [row["isbn"] for row in visible]
    assert len(isbns) == 8, (
        f"Esperava-se 8 títulos com base nos dados SQL fornecidos, "
        f"mas foram encontrados {len(isbns)}."
    )

# Availability information in available in present iteration
# So, "NotImplementedError" is replaced by actual checks on the "disponivel" field of the titles.
# Behaveor requirement only tests availability, not full status ('disponível' and 'não disponível' instead of 'emprestado', 'retirado', etc.).
@then("apresenta também os títulos que não estejam disponíveis para empréstimo")
def step_then_apresenta_tambem_indisponiveis(context):    
    visible_titles = context.catalog.visible_titles
    assert visible_titles, "A lista visível está vazia."
    
    missing_field = [
        row.get("isbn", row)
        for row in visible_titles
        if "disponivel" not in row
    ]
    assert not missing_field, (
        "Existem títulos listados sem o campo 'disponivel': "
        f"{missing_field}"
    )

    unavailable_titles = [
        row
        for row in visible_titles
        if is_unavailable(row.get("disponivel"))
    ]
    assert unavailable_titles, (
        "A lista não apresenta nenhum título indisponível para empréstimo. "
        "Esperava-se pelo menos um título com disponibilidade diferente de 'disponivel'."
    )
    


@then('cada título listado apresenta os campos "titulo", "autor", "idioma", "ano_publicacao" e "disponivel"')
def step_then_campos_obrigatorios(context):
    assert_all_titles_have_fields(
        context.catalog.visible_titles,
        ["titulo", "autor", "idioma", "ano_publicacao", "disponivel"]
    )


@then("cada título listado inclui uma ligação para consulta de detalhes")
def step_then_ligacao_para_detalhes(context):
    assert_all_titles_have_details_ref(context.catalog.visible_titles)


@given("a lista de títulos foi carregada")
def step_given_lista_foi_carregada(context):
    context.catalog.load_home_page()


@when("o utilizador navega entre elementos paginados ou navegáveis da lista")
def step_when_navega_na_lista(context):
    context.ids_before_last_action = context.catalog.current_isbns().copy()
    context.catalog.navigate_list()
    context.ids_after_last_action = context.catalog.current_isbns().copy()


@then("o conjunto de títulos apresentados não é alterado")
def step_then_conjunto_nao_alterado(context):
    assert context.ids_before_last_action == context.ids_after_last_action, (
        f"A navegação alterou o conjunto de resultados. "
        f"Antes={context.ids_before_last_action}; Depois={context.ids_after_last_action}"
    )

# ------------------------------------------------------------------
# REQ-004 - Filtro de disponibilidade
# ------------------------------------------------------------------

@when('o utilizador aplica o filtro de disponibilidade para "{valor}"')
def step_when_filtra_disponibilidade(context, valor):
    result = context.catalog.apply_filter("disponivel", valor.strip().lower())
    assert result is True


@then('são apresentados apenas títulos com disponibilidade "{valor}"')
def step_then_somente_disponibilidade(context, valor):
    esperado = valor.strip().lower()
    for titulo in context.catalog.visible_titles:
        assert titulo["disponivel"] == esperado
