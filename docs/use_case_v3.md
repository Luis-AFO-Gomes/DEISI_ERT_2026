# Use Cases — Formato descritivo

## UC-01 — Listar títulos
- **Actor principal**: Utilizador anónimo
- **Função/Actor de apoio**: Sócios validados
- **Objectivo**: Permitir ao utilizador visualizar a lista de títulos disponíveis
- **Pré-condições**: Existem títulos na plataforma
- **Trigger**: O utilizador acede ao catálogo de títulos
- **Pós-condições (success)**: A lista de títulos é exibida ao utilizador;<br>O utilizador pode ordenar e filtrar a lista de títulos
- **Pós-condições (failure/cancel)**: A lista não é apresentada, com indicação de títulos indisponíveis ou erro de acesso
- **Requisitos relacionados**: REQ-001, REQ-002, REQ-003

### Fluxo principal (happy path)
1. Actor acede ao catálogo de títulos
2. O apresenta a lista de títulos **existentes com indicação de disponibilidade para empréstimo**

### Fluxos alternativos
**A1. Actor selecciona uma opção de ordenação** → A lista de títulos é reordenada de acordo com a opção selecionada<br>
**A2. Actor selecciona uma opção de filtragem** → A lista de títulos é filtrada de acordo com a opção selecionada<br>
**A3. O actor selecciona um título específico** → O sistema apresenta os detalhes do título selecionado<br>
**A3.1. Se o actor for sócio validado** → O sistema apresenta opções adicionais nos detalhes, como exemplares disponíveis<br>
**A.3.1.1. Existem exemplares disponíveis** → O sistema apresenta a opção de reserva do título<br>
**A.3.2. Se o actor for anónimo** → O sistema apresenta apenas os detalhes básicos do título, sem opções de reserva mas com opção para registo de candidatura a sócio


### Exceptions / errors
**E1. Não existem títulos disponíveis** → O sistema apresenta uma mensagem indicando que não há títulos disponíveis<br>
**E2. Erro de acesso ao catálogo** → O sistema apresenta uma mensagem de erro e sugere tentar novamente mais tarde ou contactar o suporte

## UC-02 — Inserir títulos
- **Actor principal**: Sócio validado
- **Função/Actor de apoio**: N/A
- **Objectivo**: Permitir ao utilizador inserir novos títulos na plataforma
- **Pré-condições**: 
  - O actor principal está autenticado como sócio validado
  - Existem listas de selecção com dados pré-existentes para preenchimento de atributos de título (e.g. editoras, autores, temas, idiomas, tipos)
- **Trigger**: O utilizador acede à funcionalidade de inserção de títulos a partir do menu de navegação da plataforma
- **Pós-condições (success)**: O título é adicionado à plataforma com estado 'pendente' e fica disponível para avaliação por outros sócios e administradores;
- **Pós-condições (failure/cancel)**: O título não é adicionado, com indicação não registada de erro ou cancelamento
- **Requisitos relacionados**: REQ-008, REQ-009, REQ-011, REQ-012, REQ-013, REQ-014, REQ-015, REQ-016

### Fluxo principal (happy path)
1. Actor acede à funcionalidade de inserção de títulos
2. O actor fornece os detalhes do novo título, incluindo os seguintes atributos obrigatórios: título, editora, autor, tema, idioma e tipo. 
   1. O sistema apresenta listas de selecção para os atributos editora, autor, tema, idioma e tipo
3. O sistema valida os dados fornecidos
4. O sistema adiciona o título à plataforma com estado 'pendente' e confirma a operação

### Fluxos alternativos
**A1. A Editora pretendida pelo actor não existe na lista de selecção**
1. → O sistema apresenta uma opção para adicionar uma nova editora<br>
2. → Optando pela inserção de uma nova editora, o sistema apresenta um formulário para adicionar nova editora (REQ-011)<br>
3. → Após inserção de nova editora, a lista de selecção é actualizada e o actor pode continuar a inserção do título<br>
   
**A2. O Autor pretendido pelo actor não existe na lista de selecção**
1. → O sistema apresenta uma opção para adicionar um novo autor<br>
2. → Optando pela inserção de um novo autor, o sistema apresenta um formulário para adicionar novo autor (REQ-012)<br>
3. → Após inserção de novo autor, a lista de selecção é actualizada e o actor pode continuar a inserção do título<br>

**A3. O Tema/classificação pretendido pelo actor não existe na lista de selecção**
1. → O sistema apresenta uma opção para adicionar um novo tema/classificação<br>
2. → Optando pela inserção de um novo tema/classificação, o sistema apresenta um formulário para adicionar novo tema/classificação (REQ-013)<br>
3. → Após inserção de novo tema/classificação, a lista de selecção é actualizada e o actor pode continuar a inserção do título<br>

**A4. O Idioma pretendido pelo actor não existe na lista de selecção**
1. → O sistema apresenta uma opção para adicionar um novo idioma<br>
2. → Optando pela inserção de um novo idioma, o sistema apresenta um formulário para adicionar novo idioma (REQ-014)<br>
3. → Após inserção de novo idioma, a lista de selecção é actualizada e o actor pode continuar a inserção do título<br>

**A5. O Tipo/Formato pretendido pelo actor não existe na lista de selecção**
1. → O sistema apresenta uma opção para adicionar um novo tipo/formato<br>
2. → Optando pela inserção de um novo tipo/formato, o sistema apresenta um formulário para adicionar novo tipo/formato (REQ-015)<br>
3. → Após inserção de novo tipo/formato, a lista de selecção é actualizada e o actor pode continuar a inserção do título<br>

**A6. O título inserido já existe na plataforma (ISBN igual)** → O sistema apresenta uma mensagem indicando que o título já existe e oferece a opção de incrementar a contagem de exemplares (REQ-009)<br>
O título mantém os dados existentes, mesmo que diferentes dos inseridos até ao momento pelo actor,incrementando a contagem de exemplares e confirmando a operação ao actor<br>

**A7. A qualquer momento da inserção, o actor pode cancelar a operação** → O sistema descarta os dados inseridos e retorna à lista de títulos<br>

### Exceptions / errors
**E1. O sistema detecta dados inválidos ou incompletos** → O sistema apresenta mensagens de erro específicas para cada campo com problemas, indicando o que deve ser corrigido para prosseguir<br>
**E2. Erro de gravação** → O sistema apresenta uma mensagem de erro e sugere tentar novamente mais tarde ou contactar o suporte

## UC-03 — validar por administrador de títulos inseridos por sócios
- **Actor principal**: Administradores da plataforma
- **Função/Actor de apoio**: N/A
- **Objectivo**: Permitir a validação de títulos préviamente inseridos por sócios, garantindo que os mesmos têm dados precisos, completos e válidos antes de serem disponibilizados para consulta
- **Pré-condições**: 
  - O actor principal está autenticado como administrador da plataforma
  - O título a validar foi préviamente inserido e encontra-se em estado 'pendente' ou 'suspenso'na plataforma
- **Trigger**: O utilizador acede à área de validação de títulos e consulta a lista de títulos pendentes
- **Pós-condições (success)**: 
  - O título é adicionado à plataforma e fica disponível para consulta
  - Os dados do título são precisos, completos e válidos.
  - Todas as intervenções ficam registadas na plataforma para consulta e análise futura
- **Pós-condições (failure/cancel)**: O título não é adicionado, com indicação de erro ou cancelamento
  - O sócio que inseriu o título recebe feedback detalhado sobre as avaliações
  - Todas as intervenções ficam registadas na plataforma para consulta e análise futura
- **Requisitos relacionados**: REQ-008, REQ-011, REQ-012, REQ-013, REQ-014, REQ-015, REQ-016

### Fluxo principal (happy path)
1. Actor acede à lista de títulos pendentes de validação
2. Actor selecciona um título específico para avaliação
3. O actor valida o título e fornece feedback detalhado
4. O sistema valida os dados fornecidos
5. O sistema actualiza o título na plataforma, alterando o estado para 'disponível' e confirmando a operação ao actor
6. O sistema comunica o resultado da avaliação ao sócio que inseriu o título, incluindo feedback detalhado
7. O título passa a estar disponível para consulta, com os dados precisos, completos e válidos

### Fluxos alternativos
**A1. O actor avalia o título com tendo pequenas inconsistências ou omissões, necessitando de correcções** 

3. → O utilizador efectua as correções necessárias e submete novamente para validação
4. O sistema valida os dados fornecidos
5. O sistema actualiza o título na plataforma, mantendo o estado 'pendente', e confirma a operação
6. O sistema comunica o resultado da avaliação ao sócio que inseriu o título, incluindo feedback detalhado sobre as correções necessárias para aprovação
7. O título não é disponibilizado para consulta até nova validação bem sucedida<br>

**A1.1. A Editora pretendida pelo actor não existe na lista de selecção**
1. → O sistema apresenta uma opção para adicionar uma nova editora<br>
2. → Optando pela inserção de uma nova editora, o sistema apresenta um formulário para adicionar nova editora (REQ-011)<br>
3. → Após inserção de nova editora, a lista de selecção é actualizada e o actor pode continuar a inserção do título<br>
   
**A1.2. O Autor pretendido pelo actor não existe na lista de selecção**
1. → O sistema apresenta uma opção para adicionar um novo autor<br>
2. → Optando pela inserção de um novo autor, o sistema apresenta um formulário para adicionar novo autor (REQ-012)<br>
3. → Após inserção de novo autor, a lista de selecção é actualizada e o actor pode continuar a inserção do título<br>

**A1.3. O Tema/classificação pretendido pelo actor não existe na lista de selecção**
1. → O sistema apresenta uma opção para adicionar um novo tema/classificação<br>
2. → Optando pela inserção de um novo tema/classificação, o sistema apresenta um formulário para adicionar novo tema/classificação (REQ-013)<br>
3. → Após inserção de novo tema/classificação, a lista de selecção é actualizada e o actor pode continuar a inserção do título<br>

**A1.4. O Idioma pretendido pelo actor não existe na lista de selecção**
1. → O sistema apresenta uma opção para adicionar um novo idioma<br>
2. → Optando pela inserção de um novo idioma, o sistema apresenta um formulário para adicionar novo idioma (REQ-014)<br>
3. → Após inserção de novo idioma, a lista de selecção é actualizada e o actor pode continuar a inserção do título<br>

**A1.5. O Tipo/Formato pretendido pelo actor não existe na lista de selecção**
1. → O sistema apresenta uma opção para adicionar um novo tipo/formato<br>
2. → Optando pela inserção de um novo tipo/formato, o sistema apresenta um formulário para adicionar novo tipo/formato (REQ-015)<br>
3. → Após inserção de novo tipo/formato, a lista de selecção é actualizada e o actor pode continuar a inserção do título<br>

**A1.6. O título inserido já existe na plataforma (ISBN igual)** → O sistema apresenta uma mensagem indicando que o título já existe e oferece a opção de incrementar a contagem de exemplares (REQ-009)<br>
O título mantém os dados existentes, mesmo que diferentes dos inseridos até ao momento pelo actor,incrementando a contagem de exemplares e confirmando a operação ao actor<br>

**A2. O actor avalia o título como tendo problemas graves ou sendo inadequado para a plataforma** 

1. → O utilizador rejeita o título
2. → O sistema actualiza o título na plataforma com o estado 'rejeitado'
3. → O sistema comunica o resultado da avaliação ao sócio que inseriu o título, incluindo feedback detalhado sobre as correções necessárias para aprovação
4. → O título não é disponibilizado para consulta até nova validação bem sucedida<br>

**A3. A qualquer momento da inserção, o actor pode cancelar a operação** → O sistema descarta os dados inseridos e retorna à lista de pendentes<br>

### Exceptions / errors
**E1. O sistema detecta dados inválidos ou incompletos** → O sistema apresenta mensagens de erro específicas para cada campo com problemas, indicando o que deve ser corrigido para prosseguir<br>
**E2. Erro de gravação** → O sistema apresenta uma mensagem de erro e sugere tentar novamente mais tarde ou contactar o suporte

## UC-04 — validar por sócios de títulos inseridos por outrossócios
- **Actor principal**: Sócios validado não administradores
- **Função/Actor de apoio**: Administradores da plataforma
- **Objectivo**: Permitir a validação de títulos préviamente inseridos por sócios, garantindo que os mesmos têm dados precisos, completos e válidos antes de serem disponibilizados para consulta
- **Pré-condições**: 
  - O actor principal está autenticado como sócio validado da plataforma
  - O título a validar foi préviamente inserido e encontra-se em estado 'pendente' na plataforma
- **Trigger**: O utilizador acede à área de validação de títulos e consulta a lista de títulos pendentes
- **Pós-condições (success)**: 
  - O título é adicionado à plataforma e fica disponível para consulta
  - Os dados do título são precisos, completos e válidos.
  - Todas as intervenções ficam registadas na plataforma para consulta e análise futura
- **Pós-condições (failure/cancel)**: 
  - O título não é adicionado, com indicação de erro, cancelamento ou suspensão
  - O sócio que inseriu o título recebe feedback detalhado sobre as avaliações
  - Todas as intervenções ficam registadas na plataforma para consulta e análise futura
- **Requisitos relacionados**: REQ-008, REQ-011, REQ-012, REQ-013, REQ-014, REQ-015, REQ-016

### Fluxo principal (happy path)
1. Actor acede à lista de títulos pendentes de validação
2. Actor selecciona um título específico para avaliação
3. O actor valida o título e fornece feedback detalhado
4. O sistema valida os dados fornecidos
5. O sistema actualiza o título na plataforma, registando uma avaliação valida e mantendo o estado 'pendente', confirmando a operação ao actor
6. O sistema regista a avaliação para consulta futura
