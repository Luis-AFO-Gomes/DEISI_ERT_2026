Feature: REQ-004 - Filtrar por disponibilidade
  Como utilizador
  Quero filtrar livros por disponibilidade
  Para identificar títulos disponíveis para empréstimo

  Scenario: Filtrar livros disponíveis
    Given a lista de títulos foi carregada
    When o utilizador aplica o filtro de disponibilidade para "disponivel"
    Then são apresentados apenas títulos com disponibilidade "disponivel"

  Scenario: Filtrar livros indisponíveis
    Given a lista de títulos foi carregada
    When o utilizador aplica o filtro de disponibilidade para "emprestado"
    Then são apresentados apenas títulos com disponibilidade "emprestado"
