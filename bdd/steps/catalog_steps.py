# -*- coding: utf-8 -*-
# requer a instalação do pacote "behave" (pip install behave) no ambiente de desenvolvimento (preferencialemnte num virtualenv)
from behave import given, when, then
import unicodedata


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


def assert_titles_match_filter(titles, field, raw_value):
    expected = normalize_text(raw_value)
    for title in titles:
        actual = normalize_text(title.get(field, ""))
        assert expected in actual, (
            f"O registo não respeita o filtro {field}='{raw_value}': {title}"
        )


def assert_titles_match_all_filters(titles, filters):
    for title in titles:
        for field, raw_value in filters.items():
            expected = normalize_text(raw_value)
            actual = normalize_text(title.get(field, ""))
            assert expected in actual, (
                f"O registo não respeita todos os filtros activos. "
                f"Campo={field}, valor='{raw_value}', título={title}"
            )


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

    # Com a estrutura actual, assumimos que todos os livros da tabela livro
    # devem ser apresentados no catálogo.
    isbns = [row["isbn"] for row in visible]
    assert len(isbns) == 8, (
        f"Esperava-se 8 títulos com base nos dados SQL fornecidos, "
        f"mas foram encontrados {len(isbns)}."
    )


@then("apresenta também os títulos que não estejam disponíveis para empréstimo")
def step_then_apresenta_tambem_indisponiveis(context):
    raise NotImplementedError(
        "Critério pendente: o esquema actual não contém informação de "
        "disponibilidade/emprestável/cópias/estado de empréstimo."
    )


@then('cada título listado apresenta os campos "titulo", "autor", "idioma" e "ano_publicacao"')
def step_then_campos_obrigatorios(context):
    assert_all_titles_have_fields(
        context.catalog.visible_titles,
        ["titulo", "autor", "idioma", "ano_publicacao"]
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
# REQ-002 - Ordenar lista
# ------------------------------------------------------------------

@given("a lista de títulos está carregada no ecrã")
def step_given_lista_carregada_no_ecra(context):
    context.catalog.load_home_page()


@given('a lista apresenta os campos "titulo", "autor", "idioma" e "ano_publicacao"')
def step_given_lista_apresenta_campos(context):
    assert context.catalog.list_loaded, "A lista ainda não foi carregada."
    assert context.catalog.default_fields == ["titulo", "autor", "idioma", "ano_publicacao"]


@when('o utilizador selecciona a ordenação por "{campo}" em sentido "{sentido}"')
def step_when_selecciona_ordenacao(context, campo, sentido):
    context.ids_before_last_action = sorted(context.catalog.current_isbns())
    context.catalog.set_order(campo, sentido)
    context.ids_after_last_action = sorted(context.catalog.current_isbns())


@given('o utilizador seleccionou anteriormente a ordenação por "{campo}" em sentido "{sentido}"')
def step_given_ordenacao_anterior(context, campo, sentido):
    context.catalog.set_order(campo, sentido)


@then('a lista é reordenada pelo campo "{campo}" em sentido "{sentido}"')
def step_then_lista_reordenada(context, campo, sentido):
    reverse = sentido == "descendente"
    values = [normalize_text(row[campo]) for row in context.catalog.visible_titles]
    expected = sorted(values, reverse=reverse)

    assert values == expected, (
        f"A lista não está correctamente ordenada por {campo} ({sentido}).\n"
        f"Actual={values}\n"
        f"Esperado={expected}"
    )

    assert context.catalog.order_field == campo
    assert context.catalog.order_direction == sentido


@then("o conteúdo da lista não é alterado")
def step_then_conteudo_lista_nao_alterado(context):
    assert context.ids_before_last_action == context.ids_after_last_action, (
        f"O conteúdo da lista foi alterado. "
        f"Antes={context.ids_before_last_action}; Depois={context.ids_after_last_action}"
    )


@then('a ordenação anterior por "{campo}" deixa de estar activa')
def step_then_ordenacao_anterior_deixa_ativa(context, campo):
    assert context.catalog.order_field != campo, (
        f"A ordenação anterior por '{campo}' continua activa."
    )


@when("o utilizador visualiza a lista ordenada")
def step_when_visualiza_lista_ordenada(context):
    assert context.catalog.list_loaded, "A lista ordenada não está carregada."


@then('a lista mantém os campos "titulo", "autor", "idioma" e "ano_publicacao"')
def step_then_lista_mantem_campos(context):
    assert context.catalog.default_fields == ["titulo", "autor", "idioma", "ano_publicacao"]


@then("a lista mantém as opções disponíveis na lista padrão")
def step_then_lista_mantem_opcoes(context):
    assert context.catalog.default_options == [
        "consultar_detalhes", "ordenar", "filtrar", "navegar"
    ]


@then("cada título listado continua a incluir ligação para consulta de detalhes")
def step_then_cada_titulo_continua_com_detalhes(context):
    assert_all_titles_have_details_ref(context.catalog.visible_titles)


# ------------------------------------------------------------------
# REQ-003 - Filtrar lista
# ------------------------------------------------------------------

@when('o utilizador aplica um filtro válido por "{campo}" com o valor "{valor}"')
@given('o utilizador aplica um filtro válido por "{campo}" com o valor "{valor}"')
def step_aplica_filtro_valido(context, campo, valor):
    context.ids_before_last_action = context.catalog.current_isbns().copy()
    context.last_action_result = context.catalog.apply_filter(campo, valor)
    context.ids_after_last_action = context.catalog.current_isbns().copy()

    assert context.last_action_result is True, (
        f"O filtro deveria ter sido aplicado: {campo}={valor}"
    )


@then("a lista é reconstruída")
def step_then_lista_reconstruida(context):
    assert context.catalog.list_loaded is True
    assert isinstance(context.catalog.visible_titles, list)


@then('são apresentados apenas os títulos que obedecem ao filtro por "{campo}" com o valor "{valor}"')
def step_then_apenas_titulos_filtrados(context, campo, valor):
    assert_titles_match_filter(context.catalog.visible_titles, campo, valor)


@when('o utilizador aplica um novo filtro válido por "{campo}" com o valor "{valor}"')
def step_when_aplica_novo_filtro(context, campo, valor):
    result = context.catalog.apply_filter(campo, valor)
    assert result is True, f"O novo filtro deveria ter sido aplicado: {campo}={valor}"


@then("são apresentados apenas os títulos que obedecem simultaneamente aos filtros activos")
def step_then_filtros_cumulativos(context):
    assert_titles_match_all_filters(context.catalog.visible_titles, context.catalog.filters)


@when('o utilizador introduz no filtro por "{campo}" o valor "{valor}"')
def step_when_introduz_valor_filtro(context, campo, valor):
    context.ids_before_last_action = context.catalog.current_isbns().copy()
    context.last_action_result = context.catalog.apply_filter(campo, valor)
    context.ids_after_last_action = context.catalog.current_isbns().copy()


@then("esse filtro não é aplicado")
def step_then_filtro_nao_aplicado(context):
    assert context.last_action_result is False, "O filtro não deveria ter sido aplicado."


@then("a lista mantém o conteúdo anterior")
def step_then_lista_mantem_conteudo_anterior(context):
    assert context.ids_before_last_action == context.ids_after_last_action, (
        f"O conteúdo da lista foi alterado indevidamente. "
        f"Antes={context.ids_before_last_action}; Depois={context.ids_after_last_action}"
    )


@then('a lista filtrada mantém a ordenação por "{campo}" em sentido "{sentido}"')
def step_then_mantem_ordenacao_apos_filtro(context, campo, sentido):
    assert context.catalog.order_field == campo
    assert context.catalog.order_direction == sentido

    reverse = sentido == "descendente"
    values = [normalize_text(row[campo]) for row in context.catalog.visible_titles]
    expected = sorted(values, reverse=reverse)

    assert values == expected, (
        f"A lista filtrada não manteve a ordenação por {campo} ({sentido})."
    )


@when("a lista filtrada é apresentada")
def step_when_lista_filtrada_apresentada(context):
    assert context.catalog.visible_titles is not None


@then("cada título apresentado continua a incluir ligação para consulta de detalhes")
def step_then_titulos_filtrados_com_detalhes(context):
    assert_all_titles_have_details_ref(context.catalog.visible_titles)