@REQ-003 @catalogo @filtro
Feature: Filtrar lista de títulos
  Como visitante
  Quero filtrar a lista de títulos
  Para reduzir a lista apresentada e encontrar títulos relevantes

  Background:
    Given existem títulos em catálogo
    And a lista de títulos está carregada no ecrã
    And a lista apresenta os campos "titulo", "autor", "idioma" e "ano_publicacao"

  Scenario: Aplicar um filtro válido e reconstruir a lista
    When o utilizador aplica um filtro válido por "titulo" com o valor "bases"
    Then a lista é reconstruída
    And são apresentados apenas os títulos que obedecem ao filtro por "titulo" com o valor "bases"

  Scenario: Aplicar filtros de forma cumulativa
    Given o utilizador aplicou um filtro válido por "titulo" com o valor "bases"
    When o utilizador aplica um novo filtro válido por "autor" com o valor "Luis"
    Then a lista é reconstruída
    And são apresentados apenas os títulos que obedecem simultaneamente aos filtros activos

  Scenario: Não aplicar filtro com menos de 4 caracteres
    When o utilizador introduz no filtro por "titulo" o valor "bas"
    Then esse filtro não é aplicado
    And a lista mantém o conteúdo anterior

  Scenario: Aplicar filtro ao 4º caracteres inserido
    When o utilizador introduz no filtro por "titulo" o valor "base"
    Then esse filtro é aplicado
    And a lista é reconstruída    

  Scenario: Manter a última ordenação após aplicar filtros
    Given o utilizador seleccionou a ordenação por "autor" em sentido "ascendente"
    When o utilizador aplica um filtro válido por "titulo" com o valor "bases"
    Then a lista filtrada mantém a ordenação por "autor" em sentido "ascendente"

  Scenario: Manter estrutura e navegabilidade após filtragem
    Given o utilizador aplica um filtro válido por "titulo" com o valor "bases"
    When a lista filtrada é apresentada
    Then a lista mantém os campos "titulo", "autor", "idioma" e "ano_publicacao"
    And a lista mantém as opções disponíveis na lista padrão
    And cada título apresentado continua a incluir ligação para consulta de detalhes