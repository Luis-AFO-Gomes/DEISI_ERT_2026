# Lista de Casos de Teste

## TC-001 — Apresentar todos os títulos em catálogo

**Related requirements:** REQ-001  
**Type:** Unit/Acceptance  
**Priority:** H  

### Preconditions
- Existem títulos em catálogo.
- O utilizador encontra-se na página inicial.

### Test data
- Catálogo com vários títulos.
- Deve incluir títulos disponíveis e títulos indisponíveis para empréstimo.

### Steps
1. Aceder à página inicial.
2. Carregar a lista de títulos.

### Expected results
- O sistema apresenta todos os títulos existentes em catálogo.
- O sistema apresenta também os títulos que não estejam disponíveis para empréstimo.

---

## TC-002 — Apresentar os dados obrigatórios de cada título listado

**Related requirements:** REQ-001  
**Type:** Acceptance  
**Priority:** H  

### Preconditions
- Existem títulos em catálogo.
- O utilizador encontra-se na página inicial.

### Test data
- Títulos com os seguintes campos preenchidos (para o presente teste, os restantes atributos de cada título podem ser ignorados):
  - `titulo`
  - `autor`
  - `idioma`
  - `ano_publicacao`
- 'ano_publicacao' não é obrigatório na inserção de títulos. Na lista de teste deve existir, pelo menos, um título com o campo preenchido e outro título com o campo vazio para verificar a apresentação correta em ambos os casos. 

### Steps
1. Aceder à página inicial.
2. Carregar a lista de títulos.
3. Verificar os dados apresentados em cada título listado.

### Expected results
- Cada título listado apresenta os campos `titulo`, `autor`, `idioma` e `ano_publicacao`.
- O campo `ano_publicacao` é apresentado com indicação 'desconhecido' para os títulos que não tenham este campo preenchido.

---

## TC-003 — Disponibilizar acesso aos detalhes de cada título

**Related requirements:** REQ-001  
**Type:** UnitAcceptance  
**Priority:** M  

### Preconditions
- Existem títulos em catálogo.
- O utilizador encontra-se na página inicial.

### Test data
- Catálogo com pelo menos um título registado.

### Steps
1. Aceder à página inicial.
2. Carregar a lista de títulos.
3. Verificar se cada título possui ligação para consulta de detalhes.

### Expected results
- Cada título listado inclui uma ligação para consulta dos respetivos detalhes.

---

## TC-004 — Navegar na lista sem alterar o conteúdo apresentado

**Related requirements:** REQ-001  
**Type:** Acceptance  
**Priority:** M  

### Preconditions
- Existem títulos em catálogo.
- O utilizador encontra-se na página inicial.
- A lista de títulos foi carregada.

### Test data
- Catálogo com títulos suficientes para permitir paginação ou navegação entre elementos.

### Steps
1. Aceder à página inicial.
2. Carregar a lista de títulos.
3. Navegar entre elementos paginados ou navegáveis da lista.
4. Comparar o conjunto de títulos antes e depois da navegação.

### Expected results
- O conjunto de títulos apresentados, bem como a informação de cada um, não é alterado pela navegação.

---

## TC-005 — Ordenar lista por título em sentido ascendente

**Related requirements:** REQ-001, REQ-002  
**Type:** Integration  
**Priority:** H  

### Preconditions
- Existem títulos em catálogo.
- A lista de títulos está carregada no ecrã.
- A lista apresenta os campos `titulo`, `autor`, `idioma` e `ano_publicacao`.

### Test data
- Catálogo com múltiplos títulos com valores diferentes no campo `titulo`.

### Steps
1. Selecionar a ordenação pelo campo `titulo`.
2. Selecionar o sentido `ascendente`.

### Expected results
- A lista é reordenada pelo campo `titulo` em sentido ascendente.
- O conteúdo da lista não é alterado.

---

## TC-006 — Ordenar lista por título em sentido descendente

**Related requirements:** REQ-001, REQ-002  
**Type:** Integration  
**Priority:** H  

### Preconditions
- Existem títulos em catálogo.
- A lista de títulos está carregada no ecrã.
- A lista apresenta os campos `titulo`, `autor`, `idioma` e `ano_publicacao`.

### Test data
- Catálogo com múltiplos títulos com valores diferentes no campo `titulo`.

### Steps
1. Selecionar a ordenação pelo campo `titulo`.
2. Selecionar o sentido `descendente`.

### Expected results
- A lista é reordenada pelo campo `titulo` em sentido descendente.
- O conteúdo da lista não é alterado.

---

## TC-007 — Ordenar lista por autor em sentido ascendente

**Related requirements:** REQ-001, REQ-002  
**Type:** Integration  
**Priority:** H  

### Preconditions
- Existem títulos em catálogo.
- A lista de títulos está carregada no ecrã.
- A lista apresenta os campos `titulo`, `autor`, `idioma` e `ano_publicacao`.

### Test data
- Catálogo com múltiplos títulos com valores diferentes no campo `autor`.

### Steps
1. Selecionar a ordenação pelo campo `autor`.
2. Selecionar o sentido `ascendente`.

### Expected results
- A lista é reordenada pelo campo `autor` em sentido ascendente.
- O conteúdo da lista não é alterado.

---

## TC-008 — Ordenar lista por autor em sentido descendente

**Related requirements:** REQ-001, REQ-002  
**Type:** Integration  
**Priority:** H  

### Preconditions
- Existem títulos em catálogo.
- A lista de títulos está carregada no ecrã.
- A lista apresenta os campos `titulo`, `autor`, `idioma` e `ano_publicacao`.

### Test data
- Catálogo com múltiplos títulos com valores diferentes no campo `autor`.

### Steps
1. Selecionar a ordenação pelo campo `autor`.
2. Selecionar o sentido `descendente`.

### Expected results
- A lista é reordenada pelo campo `autor` em sentido descendente.
- O conteúdo da lista não é alterado.

---
**NOTA**
- Os casos de teste TC-005 a TC-008 podem ser classificados como unitários se a ordenação for implementada no frontend, isolando a lógica de ordenação da camada de apresentação, ou como de integração se a ordenação for implementada no backend. Caso se opte por essa abordagem, o REQ-001 deixa de ser considerado como requisito associado.
- Os casos de testes separam a direcção da ordenação para maior clareza, mas podem ser testados num caso único com a direcção a funcionar como parâmetro.
- As duas notas anteriores podem ser realizados de forma cumulativa, ou seja, podem descrever a direcção de ordenação como testes unitários ou de integração.
  
---

## TC-009 — Substituir a ordenação anterior por uma nova ordenação

**Related requirements:** REQ-001, REQ-002  
**Type:** Acceptance  
**Priority:** H  

### Preconditions
- Existem títulos em catálogo.
- A lista de títulos está carregada no ecrã.
- A lista apresenta os campos `titulo`, `autor`, `idioma` e `ano_publicacao`.
- O utilizador selecionou anteriormente a ordenação por `titulo` em sentido `ascendente`.

### Test data
- Catálogo com múltiplos títulos e autores diferentes.

### Steps
1. Confirmar que a lista está ordenada por `titulo` em sentido `ascendente`.
2. Selecionar a ordenação por `autor`.
3. Selecionar o sentido `descendente`.

### Expected results
- A lista é reordenada pelo campo `autor` em sentido descendente.
- A ordenação anterior por `titulo` deixa de estar ativa.
- O conteúdo da lista não é alterado.

---

## TC-010 — Manter os campos obrigatórios após ordenação

**Related requirements:** REQ-001, REQ-002  
**Type:** Acceptance  
**Priority:** M  

### Preconditions
- Existem títulos em catálogo.
- A lista de títulos está carregada no ecrã.
- A lista apresenta os campos `titulo`, `autor`, `idioma` e `ano_publicacao`.

### Test data
- Catálogo com múltiplos títulos.

### Steps
1. Selecionar a ordenação por `titulo` em sentido `ascendente`.
2. Verificar os campos apresentados em cada título listado.

### Expected results
- A lista mantém os campos `titulo`, `autor`, `idioma` e `ano_publicacao` após a ordenação.
- O conteúdo da lista não é alterado.

---

## TC-011 — Manter opções e navegabilidade da lista após ordenação

**Related requirements:** REQ-001, REQ-002  
**Type:** Acceptance  
**Priority:** M  

### Preconditions
- Existem títulos em catálogo.
- A lista de títulos está carregada no ecrã.
- A lista apresenta os campos `titulo`, `autor`, `idioma` e `ano_publicacao`.

### Test data
- Catálogo com múltiplos títulos, incluindo títulos com ligação para consulta de detalhes.

### Steps
1. Selecionar a ordenação por `titulo` em sentido `ascendente`.
2. Verificar se a lista mantém as opções disponíveis na lista padrão.
3. Verificar se cada título mantém ligação para consulta de detalhes.

### Expected results
- A lista mantém as opções disponíveis na lista padrão.
- Cada título listado continua a incluir ligação para consulta de detalhes.
- O conteúdo da lista não é alterado.

---
**NOTA:**
- Embora não seja solicitado, pode-se definir dependência entre casos de testes e mesmo definir uma sequência de execução - grupo ***Steps*** - que remete para outros casos de teste, evitando a repetição de passos comuns. Por exemplo, o TC-009 pode remeter paraos casos de teste TC-005 a TC-008 para substituição de ordenação, e estes podem remeter para o TC-004 para garantia de coerencia de conteúdos

---

## TC-012 — Apresentar os dados obrigatórios de cada título listado
**Substitui TC-002**<br>
**Related requirements:** REQ-001 ; REQ-002<br>
**Type:** Acceptance  
**Priority:** H  

### Preconditions
- Existem títulos em catálogo.
- O utilizador encontra-se na página inicial.

### Test data
- Títulos com os seguintes campos preenchidos (para o presente teste, os restantes atributos de cada título podem ser ignorados):
  - `titulo`
  - `autor`
  - `idioma`
  - `ano_publicacao`
  - **`disponibilidade`**
- 'ano_publicacao' não é obrigatório na inserção de títulos. Na lista de teste deve existir, pelo menos, um título com o campo preenchido e outro título com o campo vazio para verificar a apresentação correta em ambos os casos. 

### Steps
1. Aceder à página inicial.
2. Carregar a lista de títulos.
3. Verificar os dados apresentados em cada título listado.

### Expected results
- Cada título listado apresenta os campos `titulo`, `autor`, `idioma`, `ano_publicacao` e **`disponibilidade`**.
- O campo `ano_publicacao` é apresentado com indicação 'desconhecido' para os títulos que não tenham este campo preenchido.

---

## TC-013 — Manter os campos obrigatórios após ordenação
**Substitui TC-010**<br>
**Related requirements:** REQ-001, REQ-002<br>
**Type:** Acceptance  
**Priority:** M  

### Preconditions
- Existem títulos em catálogo.
- A lista de títulos está carregada no ecrã.
- A lista apresenta os campos `titulo`, `autor`, `idioma`, `ano_publicacao` e **`disponibilidade`**.

### Test data
- Catálogo com múltiplos títulos.

### Steps
1. Selecionar a ordenação por `titulo` em sentido `ascendente`.
2. Verificar os campos apresentados em cada título listado.

### Expected results
- A lista mantém os campos `titulo`, `autor`, `idioma`, `ano_publicacao` e **`disponibilidade`** após a ordenação.
- O conteúdo da lista não é alterado.

---

## TC-014 — Manter opções e navegabilidade da lista após ordenação
**Substitui TC-011**<br>
**Related requirements:** REQ-001, REQ-002<br>
**Type:** Acceptance  
**Priority:** M  

### Preconditions
- Existem títulos em catálogo.
- A lista de títulos está carregada no ecrã.
- A lista apresenta os campos `titulo`, `autor`, `idioma`, `ano_publicacao` e **`disponibilidade`**.

### Test data
- Catálogo com múltiplos títulos, incluindo títulos com ligação para consulta de detalhes.

### Steps
1. Selecionar a ordenação por `titulo` em sentido `ascendente`.
2. Verificar se a lista mantém as opções disponíveis na lista padrão.
3. Verificar se cada título mantém ligação para consulta de detalhes.

### Expected results
- A lista mantém as opções disponíveis na lista padrão.
- Cada título listado continua a incluir ligação para consulta de detalhes.
- O conteúdo da lista não é alterado.

---

## TC-015 — Filtrar a lista por disponibilidade

**Related requirements:** REQ-001, REQ-003<br>
**Type:** Acceptance  
**Priority:** M  

### Preconditions
- Existem títulos em catálogo.
- A lista de títulos está carregada no ecrã.
- A lista apresenta os campos `titulo`, `autor`, `idioma`, `ano_publicacao` e **`disponibilidade`**.

### Test data
- Catálogo com múltiplos títulos, cada um com indicação de disponibilidade, que pode ter 3 valores diferentes: disponível, emprestado, retirado.
- existe pelo menos um título para cada um dos 3 valores de disponibilidade.

### Steps
1. Selecionar , à vez, cada valor de disponibilidade.
2. Verificar se a lista é atualizada para apresentar apenas os títulos que correspondem ao valor de disponibilidade seleccionado.
3. Verificar se a lista mantém as opções disponíveis na lista padrão.
4. Verificar se cada título mantém ligação para consulta de detalhes.

### Expected results
- A lista apresenta apenas os títulos que correspondem ao valor de disponibilidade seleccionado.
- A lista mantém as opções disponíveis na lista padrão.
- Cada título listado continua a incluir ligação para consulta de detalhes.
- O conteúdo da lista não é alterado.
