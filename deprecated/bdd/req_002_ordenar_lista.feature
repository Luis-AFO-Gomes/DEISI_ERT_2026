@REQ-002 @catalogo @ordenacao
Feature: Ordenar lista de títulos
  Como visitante
  Quero ordenar a lista de títulos
  Para localizar títulos de forma mais eficiente

  Background:
    Given existem títulos em catálogo
    And a lista de títulos está carregada no ecrã
    And a lista apresenta os campos "titulo", "autor", "idioma" e "ano_publicacao"

  Scenario Outline: Ordenar a lista por um único critério e sentido
    When o utilizador selecciona a ordenação por "<campo>" em sentido "<sentido>"
    Then a lista é reordenada pelo campo "<campo>" em sentido "<sentido>"
    And o conteúdo da lista não é alterado

    Examples:
      | campo  | sentido     |
      | titulo | ascendente  |
      | titulo | descendente |
      | autor  | ascendente  |
      | autor  | descendente |

  Scenario: Substituir a ordenação anterior por uma nova ordenação
    Given o utilizador seleccionou anteriormente a ordenação por "titulo" em sentido "ascendente"
    When o utilizador selecciona a ordenação por "autor" em sentido "descendente"
    Then a lista é reordenada pelo campo "autor" em sentido "descendente"
    And a ordenação anterior por "titulo" deixa de estar activa

  Scenario: Manter estrutura e navegabilidade após ordenação
    When o utilizador selecciona a ordenação por "titulo" em sentido "ascendente"
    Then a lista mantém os campos "titulo", "autor", "idioma" e "ano_publicacao"
    And a lista mantém as opções disponíveis na lista padrão
    And cada título listado continua a incluir ligação para consulta de detalhes