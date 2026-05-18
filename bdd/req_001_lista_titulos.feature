@REQ-001 @catalogo @lista
Feature: Lista de títulos
  Como visitante
  Quero visualizar a lista de títulos na página inicial
  Para consultar o catálogo disponível

  Background:
    Given existem títulos em catálogo
    And o utilizador encontra-se na página inicial

  Scenario: Apresentar todos os títulos em catálogo
    When a página inicial é carregada
    Then o sistema apresenta todos os títulos em catálogo
    And apresenta também os títulos que não estejam disponíveis para empréstimo

  Scenario: Apresentar os dados obrigatórios de cada título listado
    When a página inicial é carregada
    Then cada título listado apresenta os campos "titulo", "autor", "idioma", "ano_publicacao" e "disponivel"

  Scenario: Disponibilizar acesso aos detalhes de cada título
    When a página inicial é carregada
    Then cada título listado inclui uma ligação para consulta de detalhes

  Scenario: Navegar na lista sem alterar o conteúdo apresentado
    Given a lista de títulos foi carregada
    When o utilizador navega entre elementos paginados ou navegáveis da lista
    Then o conjunto de títulos apresentados não é alterado