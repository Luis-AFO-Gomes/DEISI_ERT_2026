# Descrição de requisitos

## REQ-001: Lista de títulos
**Descrição**: Enquanto **Utilizador do sistema** pretendo **Listar todos os livros existentes** de modo a poder **Consultar títulos disponíveis**<br>
Na lista deve ser apresentado o título do livro, autor principal, idioma e data de publicação<br>
**Tipo**: Funcional<br>
**Stakeholder**: (anónimo)<br>
**Prioridade**: Must have<br>
**Esforço**: XL<br>
**Variant?**: Sim<br>
**Critérios de Aceitação**:
- Sempre que solicitado, o sistema apresenta a lista de livros existente
- A lista é navegável sem alterar conteúdos

## REQ-002: Ordenar lista
**Descrição**: Enquanto **utilizador da plataforma** pretendo que a **lista seja ordenável** para **facilitar a identificação de títulos existentes**<br>
A lista pode ser ordenada por título ou autor<br>
**Tipo**: Funcional<br>
**Stakeholder**: (anónimo)<br>
**Prioridade**: Could have<br>
**Esforço**: M<br>
**Variant?**: Sim<br>
**Critérios de Aceitação**:
- Por defeito, a lista é ordenada por autor
- Seleccionando o campo de ordenação, a apresentação da lista é alterada para ser apresentada ordenada pelo campo seleccionado
- A lista pode ser ordenada ascendentemente ou descendentemente por qualquer dos campos de ordenação
- Não há ordenações compostas
  
## REQ-003: Filtrar lista
**Descrição**: Enquanto **utilizador da plataforma** pretendo que a **lista seja filtrável** para **facilitar a identificação de títulos existentes**<br>
A lista pode ser filtrada por título e/ou autor<br>
**Tipo**: Funcional<br>
**Stakeholder**: (anónimo)<br>
**Prioridade**: Should have<br>
**Esforço**: M<br>
**Variant?**: Sim<br>
**Critérios de Aceitação**:
- Por defeito, a lista é apresentada sem filtros
- Seleccionando os critérios de filtro, a apresentação da lista é alterada para ser apresentada filtrada pelos critérios seleccionados
- Os filtros são cumulativos, ou seja, é possível filtrar por título e autor ao mesmo tempo
- A lista é atualizada dinamicamente à medida que os critérios de filtro são seleccionados ou deseleccionados, é necessário o mínimo de 4 caracteres num campo de filtro para que este seja aplicado
- A aplicação de um filtro não altera a ordenação da lista, que se mantém conforme a última ordenação seleccionada
- Existe a possibilidade de filtragem avançada por campos não apresentados na lista, sendo apresentado ecrã próprio para especificação de critérios

## REQ-004: Indicação de disponibilidade de livro
**Descrição**: Enquanto **utilizador da plataforma** pretendo que a **lista indique a disponibilidade dos livros** para **facilitar a selecção do próximo empréstimo**<br>
Na versão final, a disponibilidade só deve ser apresentada nos detalhes do livro e para utilizadores autenticados, não na lista principal. No entanto, por conveniência e operacionalidade da versão actual, a disponibilidade será apresentada na lista principal com indicação {disponível; emprestado;retirado}<br>
**Tipo**: Funcional<br>
**Stakeholder**: (anónimo)<br>
**Prioridade**: Should have<br>
**Esforço**: S<br>
**Variant?**: Sim<br>
**Critérios de Aceitação**:
- A lista de livros apresenta a disponibilidade de cada livro, indicando se está disponível, emprestado ou retirado
- A indicação de disponibilidade mantém-se com ordenação e filtros
- A lista pode ser filtrada por disponibilidade
