from behave import when, then

@when('o utilizador aplica o filtro de disponibilidade para "{valor}"')
def step_when_filtra_disponibilidade(context, valor):
    result = context.catalog.apply_filter("disponivel", valor.strip().lower())
    assert result is True


@then('são apresentados apenas títulos com disponibilidade "{valor}"')
def step_then_somente_disponibilidade(context, valor):
    esperado = valor.strip().lower()
    for titulo in context.catalog.visible_titles:
        assert titulo["disponivel"] == esperado
