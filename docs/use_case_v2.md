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