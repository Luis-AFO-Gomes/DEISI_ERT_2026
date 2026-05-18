Identificação inicial de requisitos

| Item | Requisito | Tipo<br>(F/nF/S) | Stakeholder | Prioridade<br><small>(MoSCoW)</small> | Esforço<br><small>(xs...XL)</small> | Variant?<br><small>(s/n)</small> |
|---:|---|---|---|---|---|---|
| REQ-001 | O sistema deve apresentar a lista de títulos existente na página inicial | F | (anónimo) | M | XL | S |
| REQ-002 | O sistema deve permitir ordenar a lista de títulos | F | (anónimo) | S | s | S |
| REQ-003 | O sistema deve permitir filtrar a lista de títulos | F | (anónimo) | S | s | S |
| REQ-004 | Ao seleccionar um título, deve ser apresentado os detalhes | F | (anónimo) | S | L | S |
| REQ-005 | Ao apresentar os detalhes de um título, deve-se incluir o número de exemplares disponíveis para empréstimo | F | Sócio | C | S | S |
| REQ-006 | O sistema deve permitir que qualquer utilizador que lhe aceda se possa candidatar a sócio | F |Promotor | M | L | S |
| REQ-007 | Um candidato só poderá ser aceite como sócio após validação por administrador da plataforma | F | Promotor | M | L | S |
| REQ-008 | Qualquer sócio deverá poder adicionar títulos e exemplares à plataforma | F | Sócio<br>administrador | M | L | S |
| REQ-009 | Quando é adicionado um título, caso já exista, deve-se manter o existente incrementando a contagem de exemplares | F | Administrador | C | S | S |
| REQ-010 | A qualquer momento, o proprietario de um exemplar ou um administrador da plataforma podem retirar um exemplar de circulação | F | Sócio<br>Administrador | C | M | S |
| REQ-011 | A inserção de **TÍTULO** requer a existência de **EDITORA** | F | Sócio<br>Administrador | S | s | S |
| REQ-012 | A inserção de **TÍTULO** requer a existência de **AUTOR** | F | Sócio<br>Administrador | S | M | S |
| REQ-013 | A inserção de **TÍTULO** requer a existência de **TEMA**, referentes a categorias de arquivo bibliotecário | F | Sócio<br>Administrador | C | s | N |
| REQ-014 | A inserção de **TÍTULO** requer a existência de **IDIOMA** | F | Sócio<br>Administrador | C | xs | S |
| REQ-015 | A inserção de **TÍTULO** requer a existência de **TIPO**, referente ao formato de publicação | F | Sócio<br>Administrador | C | xs | S |
| REQ-016 | A inserção de um **TÍTULO** requer a validação por um administrador da plataforma ou por dois sócios distintos não administradores | F | Administrador | M | XL | S |
| REQ-017 | Um **TÍTULO** existente na plataforma pode ser editado por administrador ou por sócio, no segundo caso, a edição requer validação por um administrador da plataforma ou por dois sócios distintos não administradores | F | Administrador | C | XL | S |
| RNF-001 | A plataforma será desenvolvida em Python com BD MySQL | S | N/A | N/A | N/A | N/A |
| ... | ... | ... | ... | ... | ... | ... |
