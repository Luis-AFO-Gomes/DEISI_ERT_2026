# Critérios de aceitação em BDD

## REQ-001: Lista de títulos

### Scenario: Apresentar todos os títulos em catálogo

**GIVEN** que existem títulos em catálogo  
**WHEN** o utilizador acede à página inicial  
**THEN** o sistema apresenta todos os títulos em catálogo  
**AND** apresenta também os títulos que não estejam disponíveis para empréstimo  

### Scenario: Apresentar os dados essenciais de cada título

**GIVEN** que a lista de títulos é apresentada  
**WHEN** o utilizador visualiza um título da lista  
**THEN** o sistema apresenta o título  
**AND** apresenta o autor  
**AND** apresenta o idioma  
**AND** apresenta o ano de publicação
**AND** o sistema apresenta uma ligação para consultar os detalhes desse título  

### Scenario: Navegar na lista sem alterar o seu conteúdo

**GIVEN** que a lista de títulos é apresentada  
**WHEN** o utilizador navega na lista  
**THEN** o conteúdo da lista não é alterado  

---

## REQ-002: Ordenar lista

### Scenario: Reordenar a lista por um critério seleccionado

**GIVEN** que a lista de títulos está carregada no ecrã  
**WHEN** o utilizador selecciona um critério de ordenação  
**THEN** a lista é reordenada de acordo com esse critério  
**AND** o conteúdo da lista não é alterado  

### Scenario: Aplicar apenas a ordenação actualmente seleccionada

**GIVEN** que a lista já foi ordenada anteriormente  
**WHEN** o utilizador selecciona um novo critério de ordenação  
**THEN** a lista é actualizada apenas com base no novo critério  
**AND** a ordenação anterior não é mantida de forma cumulativa  

### Scenario: Manter estrutura e navegabilidade da lista após ordenação

**GIVEN** que a lista foi reordenada  
**WHEN** o utilizador visualiza a lista ordenada  
**THEN** a lista mantém os mesmos campos da lista padrão  
**AND** mantém as mesmas opções disponíveis  
**AND** mantém a mesma navegabilidade  

---

## REQ-003: Filtrar lista

### Scenario: Filtrar a lista por um critério

**GIVEN** que a lista de títulos está carregada no ecrã  
**WHEN** o utilizador aplica um critério de filtro válido  
**THEN** a lista é reconstruída  
**AND** são apresentados apenas os títulos que obedecem ao critério indicado  

### Scenario: Aplicar filtros de forma cumulativa

**GIVEN** que existe pelo menos um filtro activo  
**WHEN** o utilizador altera pelo menos um critério de filtro válido  
**THEN** a lista é reconstruída com aplicação cumulativa de todos os filtros activos  

### Scenario: Exigir comprimento mínimo para aplicar filtro textual

**GIVEN** que a lista de títulos está carregada no ecrã  
**WHEN** o utilizador introduz menos de 4 caracteres num campo de filtro  
**THEN** esse filtro não é aplicado  
**WHEN** o utilizador introduz 4 ou mais caracteres num campo de filtro  
**THEN** esse filtro é aplicado
**AND** a lista é reconstruída a cada novo carácter introduzido

### Scenario: Manter a última ordenação após aplicar filtros

**GIVEN** que a lista foi previamente ordenada  
**AND** o utilizador aplica um ou mais filtros válidos  
**WHEN** a lista é reconstruída  
**THEN** a ordenação da lista mantém-se conforme a última ordenação seleccionada  

### Scenario: Manter estrutura e navegabilidade da lista após filtragem

**GIVEN** que a lista foi filtrada  
**WHEN** o utilizador visualiza os resultados  
**THEN** a lista mantém os mesmos campos da lista padrão  
**AND** mantém as mesmas opções disponíveis  
**AND** mantém a mesma navegabilidade  
**AND** essas características aplicam-se apenas aos títulos apresentados
