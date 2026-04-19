# Matrizes de Requisitos - Versão 1.0.0
## lista de requisitos
- [REQ-001: Lista de títulos](#req-001-lista-de-títulos)
- [REQ-002: Ordenar lista](#req-002-ordenar-lista)
- [REQ-003: Filtrar lista](#req-003-filtrar-lista)  
  

## REQ-001: Lista de títulos
<table>
    <tr>
        <td><strong>ID:</strong></td>
        <td>REQ-001</td>
        <td><strong>Versão:</strong></td>
        <td>1.0.0</td>
        <td><strong>Data:</strong></td>
        <td>2026-04-01</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Nome:</strong></td>
    </tr>
    <tr>
        <td colspan="6">Listar títulos</td>
    </tr>
    <tr>
        <td><strong>Stakeholder:</strong></td>
        <td>(anónimo)</td>
        <td><strong>Prioridade:</strong></td>
        <td>M</td>
        <td><strong>Esforço:</strong></td>
        <td>XL</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Descrição:</strong></td>
    </tr>
    <tr>
        <td colspan="6">O sistema deve apresentar a lista de títulos existente na página inicial</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Objectivos:</strong></td>
    </tr>
    <tr>
        <td colspan="6">Publicitar títulos disponíveis para empréstimo<br>Permitir visualização de catálogo a utilizadores anónimos
        </td>
    </tr>
    <tr>
        <td><strong>Tipo:</strong></td>
        <td>Funcional</td>
        <td><strong>Variant?:</strong></td>
        <td>Sim</td>
        <td><strong>CSF:</strong></td>
        <td>FCS01; FCS02</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Pré-Condições:</strong></td>
    </tr>
    <tr>
        <td colspan="6">
        <ol>
            <li>Existem títulos em catálogos</li>
            <li>Não é requeriddo login</li>
        </ol>
        </td>
    </tr>
    <tr>
        <td colspan="6"><strong>Pós-Condições:</strong></td>
    </tr>
    <tr>
        <td colspan="6">Qualquer utilizador pode consultar detalhes de um título listado</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Critérios de Aceitação:</strong></td>
    </tr>
    <tr>
        <td colspan="6">
        <ol>
            <li>Todos os títulos em catálogo são apresentados, mesmo que não estejam disponíveis para empréstimo</li>
            <li>Para cada título são apresentados os seguintes dados: título, autor, idioma e data de publicação (ano)</li>
            <li>Em cada cada título da lista, inclui-se ligação para consultar detalhes</li>
            <li>A lista é navegável sem alterar conteúdos</li>
        </ol>
        </td>
    </tr>
    <tr>
        <td colspan="6"><strong>Método de validação:</strong></td>
    </tr>
    <tr>
        <td colspan="6">
        Avaliação manual por parte de stakeholders, método estático,utilizando um protótipo navegável da interface de utilizador, com dados de teste pré-carregados
        </td>
    </tr>
    <tr>
        <td colspan="6"><strong>Requisitos relacionados:</strong></td>
    </tr>
    <tr>
        <td colspan="4">Requisito</td>
        <td colspan="2">Relação</td>
    </tr>
    <tr>
        <td colspan="4"><a href="rem_v1.md#req-002-ordenar-lista">REQ-002: Ordenar lista</a></td>
        <td colspan="2">Complementar</td>
    </tr>
    <tr>
        <td colspan="4"><a href="rem_v1.md#req-003-filtrar-lista">REQ-003: Filtrar lista</a></td>
        <td colspan="2">Complementar</td>
    </tr>
</table>

--- [Voltar ao índice](#lista-de-requisitos) ---

## REQ-002: Ordenar lista
<table>
    <tr>
        <td><strong>ID:</strong></td>
        <td>REQ-002</td>
        <td><strong>Versão:</strong></td>
        <td>1.0.0</td>
        <td><strong>Data:</strong></td>
        <td>2026-04-01</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Nome:</strong></td>
    </tr>
    <tr>
        <td colspan="6">Ordenar lista</td>
    </tr>
    <tr>
        <td><strong>Stakeholder:</strong></td>
        <td>(anónimo)</td>
        <td><strong>Prioridade:</strong></td>
        <td>M</td>
        <td><strong>Esforço:</strong></td>
        <td>XL</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Descrição:</strong></td>
    </tr>
    <tr>
        <td colspan="6">O sistema deve apresentar a lista de títulos existente na página inicial</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Objectivos:</strong></td>
    </tr>
    <tr>
        <td colspan="6">Publicitar títulos disponíveis para empréstimo<br>Permitir visualização de catálogo a utilizadores anónimos
        </td>
    </tr>
    <tr>
        <td><strong>Tipo:</strong></td>
        <td>Funcional</td>
        <td><strong>Variant?:</strong></td>
        <td>Sim</td>
        <td><strong>CSF:</strong></td>
        <td>FCS01; FCS02</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Pré-Condições:</strong></td>
    </tr>
    <tr>
        <td colspan="6">
        <ol>
            <li>Existem títulos em catálogos</li>
            <li>Não é requeriddo login</li>
        </ol>
        </td>
    </tr>
    <tr>
        <td colspan="6"><strong>Pós-Condições:</strong></td>
    </tr>
    <tr>
        <td colspan="6">Qualquer utilizador pode consultar detalhes de um título listado</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Critérios de Aceitação:</strong></td>
    </tr>
    <tr>
        <td colspan="6">
        <ol>
            <li>Todos os títulos em catálogo são apresentados, mesmo que não estejam disponíveis para empréstimo</li>
            <li>Para cada título são apresentados os seguintes dados: título, autor, idioma e data de publicação (ano)</li>
            <li>Em cada cada título da lista, inclui-se ligação para consultar detalhes</li>
            <li>A lista é navegável sem alterar conteúdos</li>
        </ol>
        </td>
    </tr>
    <tr>
        <td colspan="6"><strong>Método de validação:</strong></td>
    </tr>
    <tr>
        <td colspan="6">
        Avaliação manual por parte de stakeholders, método estático,utilizando um protótipo navegável da interface de utilizador, com dados de teste pré-carregados
        </td>
    </tr>
    <tr>
        <td colspan="6"><strong>Requisitos relacionados:</strong></td>
    </tr>
    <tr>
        <td colspan="4">Requisito</td>
        <td colspan="2">Relação</td>
    </tr>
    <tr>
        <td colspan="4"><a href="rem_v1.md#req-002-ordenar-lista">REQ-002: Ordenar lista</a></td>
        <td colspan="2">Complementar</td>
    </tr>
    <tr>
        <td colspan="4"><a href="rem_v1.md#req-003-filtrar-lista">REQ-003: Filtrar lista</a></td>
        <td colspan="2">Complementar</td>
    </tr>
</table>

--- [Voltar ao índice](#lista-de-requisitos) ---

## REQ-003: Filtrar lista
<table>
    <tr>
        <td><strong>ID:</strong></td>
        <td>REQ-003</td>
        <td><strong>Versão:</strong></td>
        <td>1.0.0</td>
        <td><strong>Data:</strong></td>
        <td>2026-04-01</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Nome:</strong></td>
    </tr>
    <tr>
        <td colspan="6">Filtrar lista</td>
    </tr>
    <tr>
        <td><strong>Stakeholder:</strong></td>
        <td>(anónimo)</td>
        <td><strong>Prioridade:</strong></td>
        <td>M</td>
        <td><strong>Esforço:</strong></td>
        <td>XL</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Descrição:</strong></td>
    </tr>
    <tr>
        <td colspan="6">O sistema deve permitir filtrar a lista de títulos existente na página inicial</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Objectivos:</strong></td>
    </tr>
    <tr>
        <td colspan="6">Publicitar títulos disponíveis para empréstimo<br>Permitir visualização de catálogo a utilizadores anónimos
        </td>
    </tr>
    <tr>
        <td><strong>Tipo:</strong></td>
        <td>Funcional</td>
        <td><strong>Variant?:</strong></td>
        <td>Sim</td>
        <td><strong>CSF:</strong></td>
        <td>FCS01; FCS02</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Pré-Condições:</strong></td>
    </tr>
    <tr>
        <td colspan="6">
        <ol>
            <li>Existem títulos em catálogos</li>
            <li>Não é requeriddo login</li>
        </ol>
        </td>
    </tr>
    <tr>
        <td colspan="6"><strong>Pós-Condições:</strong></td>
    </tr>
    <tr>
        <td colspan="6">Qualquer utilizador pode consultar detalhes de um título listado</td>
    </tr>
    <tr>
        <td colspan="6"><strong>Critérios de Aceitação:</strong></td>
    </tr>
    <tr>
        <td colspan="6">
        <ol>
            <li>Todos os títulos em catálogo são apresentados, mesmo que não estejam disponíveis para empréstimo</li>
            <li>Para cada título são apresentados os seguintes dados: título, autor, idioma e data de publicação (ano)</li>
            <li>Em cada cada título da lista, inclui-se ligação para consultar detalhes</li>
            <li>A lista é navegável sem alterar conteúdos</li>
        </ol>
        </td>
    </tr>
    <tr>
        <td colspan="6"><strong>Método de validação:</strong></td>
    </tr>
    <tr>
        <td colspan="6">
        Avaliação manual por parte de stakeholders, método estático,utilizando um protótipo navegável da interface de utilizador, com dados de teste pré-carregados
        </td>
    </tr>
    <tr>
        <td colspan="6"><strong>Requisitos relacionados:</strong></td>
    </tr>
    <tr>
        <td colspan="4">Requisito</td>
        <td colspan="2">Relação</td>
    </tr>
    <tr>
        <td colspan="4"><a href="rem_v1.md#req-002-ordenar-lista">REQ-002: Ordenar lista</a></td>
        <td colspan="2">Complementar</td>
    </tr>
    <tr>
        <td colspan="4"><a href="rem_v1.md#req-003-filtrar-lista">REQ-003: Filtrar lista</a></td>
        <td colspan="2">Complementar</td>
    </tr>
</table>

--- [Voltar ao índice](#lista-de-requisitos) ---
