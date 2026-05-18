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

## REQ-011: Registo de editoras
**Descrição**: Enquanto **Responsável da plataforma** pretendo que a **exista uma lista actualizada e correcta de editoras** para **Os títulos registados tenham informação completa e precisa**<br>
O registo do livro deve incluir a seleção de uma editora existente ou a criação de uma nova editora, garantindo que todas as informações são precisas e atualizadas.<br>
O registo de uma editora inclui {NIPC; nome publico; contacto; morada}<br>
Podendo existir editoras antigas ou estrangeiras sem a informação completa (e.g. NIPC) a plataforma deve permitir o registo de editoras sem NIPC, mas garantindo que não há duplicados e que este atributi possa ser utilizado como chave<br>
**Tipo**: Funcional<br>
**Stakeholder**: promotor<br>
**Prioridade**: Should have<br>
**Esforço**: S<br>
**Variant?**: Sim<br>
**Critérios de Aceitação**:
- A lista de editoras pode ser atualizada a qualquer momento
- É possível selecionar uma editora existente ao registar um livro
- É possível criar uma nova editora ao registar um livro, garantindo que todas as informações são precisas e atualizadas
- A plataforma não permite duplicação de NIPC nem a inserção de editoras sem este atributo
- A plataforma deve disponibilizar opção para gerar NIPC para editoras sem este atributo, garantindo a unicidade e integridade dos registos de editoras. O valor gerado deve indicar que foi gerado pela plataforma e que a causa da necessidade.
- A plataforma não permite duplicação de NIPC nem a inserção de editoras sem este atributo

## REQ-012: Registo de autores
**Descrição**: Enquanto **Responsável da plataforma** pretendo que a **exista uma lista actualizada e correcta de autores** para **Os títulos registados tenham informação completa e precisa**<br>
O registo de um livro deve incluir a seleção de um autor, ou mais, existente ou a criação de um novo autor, garantindo que todas as informações são precisas e atualizadas.<br>
O registo de um autor inclui {identificador; nome publico; contacto; data de nascimento; nacionalidade}<br>
O identificador deve ser único para cada autor, garantindo a integridade dos registos. O identificador deve ser gerado pela plataforma com base no nome e data de nascimento do autor.<br>
**Tipo**: Funcional<br>
**Stakeholder**: promotor<br>
**Prioridade**: Should have<br>
**Esforço**: M<br>
**Variant?**: Sim<br>
**Critérios de Aceitação**:
- A lista de autores pode ser atualizada a qualquer momento
- É possível selecionar um autor existente ao registar um livro
- É possível criar um novo autor ao registar um livro, garantindo que todas as informações são precisas e atualizadas
- A plataforma não permite duplicação de identificador nem a inserção de autores sem este atributo
- A plataforma deve disponibilizar opção para gerar identificador para autores sem este atributo, garantindo a unicidade e integridade dos registos de autores.
- A plataforma não permite duplicação de identificador nem a inserção de autores sem este atributo

## REQ-013: Registo de Temas (Categorias de arquivo bibliotecário)
**Descrição**: Enquanto **Responsável da plataforma** pretendo que a **exista uma lista actualizada e correcta de temas** para **Os títulos registados tenham informação completa e precisa**<br>
**Tema** refere-se a uma categoria ou assunto específico que pode ser associado a um livro, devendo seguir a categorização padrão utilizada em arquivos e bibliotecas [Classificação Decimal Universal](https://pt.wikipedia.org/wiki/Classifica%C3%A7%C3%A3o_decimal_universal) [CDU].<br>
O registo de um livro deve incluir a seleção de um tema existente, ou mais, mas não a inserção de um novo tema, de modo a permitir a validação de categorias face à taxonomia padrão CDU.<br>
O registo de um tema inclui {identificador [CDU]; desiganação; descrição}<br>
**Tipo**: Funcional<br>
**Stakeholder**: promotor<br>
**Prioridade**: Could have<br>
**Esforço**: s<br>
**Variant?**: Sim<br>
**Critérios de Aceitação**:
- A lista de temas pode ser atualizada a qualquer momento
- É possível selecionar um tema existente ao registar um livro
- Não é possível adicionar um novo tema ao registar um livro
- Os temas só podem ser geridos por um administrador da plataforma ou lidos a partir de API externa certificada para aplicação de taxonomia CDU
- A plataforma não permite duplicação de identificador CDU nem a inserção de temas sem este atributo

## REQ-014: Registo de Idiomas
**Descrição**: Enquanto **Responsável da plataforma** pretendo que a **exista uma lista actualizada e correcta de Idiomas** para **Os títulos registados tenham informação completa e precisa**<br>
**Idioma** refere-se à língua específica de publicação do título, ***não*** ao idioma original de eventual tradução.<br>
Os idiomas devem seguir a codificação padrão ISO 639:2023, garantindo a consistência e interoperabilidade dos registos de idiomas.<br>
O registo de um livro deve incluir a seleção de um idioma existente, ou mais, mas não a inserção de novos idiomas, de modo a permitir a validação de categorias face à taxonomia padrão ISO 639:2023.<br>
O registo de um idioma inclui {identificador [ISO 639:2023]; designação formal; descrição}<br>
**Tipo**: Funcional<br>
**Stakeholder**: promotor<br>
**Prioridade**: Could have<br>
**Esforço**: xs<br>
**Variant?**: Sim<br>
**Critérios de Aceitação**:
- A lista de idiomas pode ser atualizada a qualquer momento
- É possível selecionar um idioma existente ao registar um livro
- Não é possível adicionar um novo idioma ao registar um livro.
- Os idiomas só podem ser geridos por um administrador da plataforma ou lidos a partir de API externa certificada para aplicação de taxonomia ISO 639:2023
- A plataforma não permite duplicação de código ISO 639:2023 nem a inserção de idiomas sem este atributo

## REQ-015: Registo de Tipos (formatos de publicação)
**Descrição**: Enquanto **Responsável da plataforma** pretendo que a **exista uma lista actualizada e correcta de Tipos** para **Os títulos registados tenham informação completa e precisa**<br>
**Tipo** refere-se ao formato específico de publicação do título, como livro impresso, e-book, audiobook, entre outros.<br>
O registo de um livro deve incluir a seleção de um tipo, e apenas um tipo, existente, mas não a inserção de novos tipos, de modo a garantir a uniformidade de formatos.<br>
Um título pode existir em vários formatos que, para efeito de registo na plataforma, são considerados como publicações distintas e sujeitas a registos independentes, isto porque os ISBN são diferentes.
O registo de um tipo inclui {identificador unico; designação; descrição}<br>
**Tipo**: Funcional<br>
**Stakeholder**: promotor<br>
**Prioridade**: Could have<br>
**Esforço**: xs<br>
**Variant?**: Sim<br>
**Critérios de Aceitação**:
- A lista de tipos pode ser atualizada a qualquer momento
- É possível selecionar um tipo existente ao registar um livro
- Não é possível adicionar um novo tipo ao registar um livro.
- Os tipos só podem ser geridos por um administrador da plataforma
- A plataforma não permite duplicação de identificador nem a inserção de tipos sem este atributo

## REQ-008: Registo de títulos
**Descrição**: Enquanto **Sócio** pretendo que a **que sejam adicionados títulos e exemplares à plataforma** para **manter a lista de títulos atualizada e precisa**<br>
Os títulos são registados indicando {ISBN, título de capa, autor(es), editora, tema(s), idioma(s), tipo, data de publicação}<br>
Caso o título seja uma tradução, deve-se indicar o original, ele próprio título registado na plataforma<br>
Os atributos {autor, editora, tema, idioma, tipo} devem ser seleccionados a partir de listas existentes, podendo ser adicionados autores ou editora se inexistentes<br>
Após registado, o título fica pendente de validação por um administrador da plataforma ou por dois sócios distintos não administradores, antes de publicação<br>
**Tipo**: Funcional<br>
**Stakeholder**: promotor<br>
**Prioridade**: Must have<br>
**Esforço**: L<br>
**Variant?**: Sim<br>
**Critérios de Aceitação**:
- O título é inserido com os atributos obrigatórios e opcionais
- Nenhum título inserido fica imediatamente publicado, todos ficam pendentes de avaliação
- Os título pendentes ficam disponíveis em área própria da plataforma, onde podem ser consultados por qualquer utilizador com permissões de acesso apropriadas. Na versão presente, a premissões necessárias e suficientes para avaliação são 'sócio' e 'administrador'
- Os atributos {autor, editora, tema, idioma, tipo} são seleccionados a partir de listas existentes.
- É possível adicionar um novo autor ou editora se inexistentes, mas não é possível adicionar um novo tema, idioma ou tipo
- A plataforma não permite a inserção de um título com ISBN já existente nem a inserção de um título sem ISBN

## REQ-016: Validação de títulos
**Descrição**: Enquanto **Promotor** pretendo que a **inserção de títulos seja validada, corrigida ou rejeitada por pares ou administradores da plataforma** para **garantir que as entradas na plataforma sejam precisas, consistentes e confiáveis**<br>
As avaliações são realizadas apartir das lista de inserções pendetes - REQ-008 - por utilizadores com permissões de acesso apropriadas. Na versão presente, a premissões necessárias e suficientes para avaliação são 'sócio' e 'administrador'<br>
Um utilizador não pode avaliar os seus próprio títulos, mesmo sendo administrador, pelo que na lista de titulos pendentes de avaliação que é mostrada a cada sócio, não constarão os títulos inseridos por esse sócio.<br>
Para cada avaliação, o avaliador deve verificar a precisão, consistência e confiabilidade das informações fornecidas, indicando, além do resultado da avaliação, feedback detalhado, particularmente em caso de correção ou rejeição em que devem ser identificadas as falhas que levaram à decisão.<br>
A avaliação pode ter como resultado a aprovação, correção ou rejeição do título, sempre com efeito imediato se efectuada por um administrador da plataforma ou requerendo corroboração de 2º avaliador quando efectuada por sócios não administradores. As avaliações por pares são cegas, i.e., não há comunicação entre os avaliadores durante o processo nem a identidade dos avaliadores é revelada. Caso a apreciação seja discordante, o titulo passa ao estado de '(avaliação) suspensa.<br>
O resultado da avaliação deve ser comunicado ao sócio que inseriu o título, incluindo feedback detalhado em caso de correção ou rejeição. O processo de avaliação deve ser transparente e documentado, permitindo a rastreabilidade das decisões tomadas pelos avaliadores.<br>
Em caso de rejeição, o título é eliminado da plataforma, mas mantendo o registo de inserção e rejeição para fins de histórico e análise de qualidade. Qualquer submissão posterior será um processo novo e independente, mesmo que iniciado por correcção das falhas apontadas na avaliação<br>
Em caso de correção, o título é atualizado conforme as sugestões dos avaliadores e submetido novamente para avaliação, mantendo o histórico de avaliações anteriores.<br>
Em caso de aprovação, o título é publicado na plataforma e passa a estar disponível para consulta e empréstimo, mantendo o histórico de avaliações para referência futura.<br>
**Tipo**: Funcional<br>
**Stakeholder**: promotor<br>
**Prioridade**: Must have<br>
**Esforço**: XL<br>
**Variant?**: Sim<br>
**Critérios de Aceitação**:
- Os título pendentes são obtidos em área própria da plataforma por qualquer utilizador com permissões de acesso apropriadas. Na versão presente, a premissões necessárias e suficientes para avaliação são 'sócio' e 'administrador'
- A lista de titulos pendentes de avaliação que é mostrada a cada sócio, não constarão os títulos inseridos por esse sócio, mesmo sendo administrador.
- Os livros suspensos só são apresentados a adminstradores
- Cada avaliador pode indicar resultados {aprovado, corrigir, rejeitado} a partir de lista não editável e inserir feedback detalhado, não sendo permitida a gravação da avaliação sem estes dois elementos
- Caso o avaliador seja administrador, os resultados da avaliação são imediatos; 
- Caso o avaliador seja um sócio não administrador, o titulo mantém o estado pendente, requerendo corroboração de um segundo avaliador não administrador
- Se a 2ª avaliação por sócio não administrador for concordante com a 1ª, o resultado é aplicado imediatamente; caso seja discordante, o titulo mantém a pendência até nova avaliação por administrador
- Os resultados de avaliações por sócios não são visiveis a outros sócios, mantendo a indicação de pendência até que haja 2ª avaliação
- O resultado da avaliação é comunicado ao sócio que inseriu o título, incluindo feedback detalhado em caso de correção ou rejeição
- Todas as intervenções ficam registadas na plataforma para consulta e análise futura