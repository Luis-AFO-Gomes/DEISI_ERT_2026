# Vision
Aplicação para gestão de bibliotecas partilhadas, onde cada membro pode colocar livro dos quais é [**proprietario**] para serem requisitados por outros

A plataforma só utiliza livros físicos, propriedade de [**Sócios**]. Não se registam nem emprestam [**Exemplares**] de terceiros nem existe um espaço físico para guardar livros, cada propriétário guardará os livros não emprestados em espaço prórpio

Não é necessário ser proprietário de livros disponibilizados para partilha para fazer parte [**socio**] do grupo

Podem existir várias cópias [**exemplares**] do mesmo livro [**titulo**]

A base da aplicação é a lista de livros disponíveis, que é publica (pode ser consultada mesmo por não sócios). Esta lista é alimentada por sócios, que disponibilizam exemplares particulares para empréstimo.
Para se fazer sócio, um utilizador tem que fazer um pedido de admissão, que será validado por um administrador da plataforma

Qualquer sócio pode solicitar empréstimo de livros

## Objectivos
### OBJ01
 - Permitir a particulares partilhar livors sem a necessidade de participação de instituição central
### OBJ02
- Partilha publica de catálogo de **Títulos** como forma de angariar **Sócios** e promover a leitura
### OBJ03
- Avaliação de livros por **Sócios**
- Partilha pública de avaliações e comentários
### OBJ04
- Facilitar a entrega de livros emprestados
- Gerir localizações de modo a optimizar entrega de empréstimos

## Notas e Assunções de projecto
- A plataforma é gratuita para os sócios, sem custos de adesão ou utilização
- A plataforma é acessível através de um website, compatível com dispositivos móveis e desktop
- Na versão inicial, a plataforma é desenvolvida em formato desktop, removendo a complexidade de implementação de infraestrutura servidor
- A plataforma não tem publicidade, nem recolhe dados pessoais dos utilizadores, para garantir a privacidade e segurança dos sócios, mas pode vir a partilhar dados de avaliação de livros para fins de recomendação e análise de tendências de leitura

## Regras de leitura de documentos:
- Utiliza-se **escala MoSCoW** para classificação de requisitos, onde:
  - **M**: Must have (Requisito obrigatório)
  - **S**: Should have (Requisito desejável, mas não essencial)
  - **C**: Could have (Requisito opcional, que pode ser incluído se houver tempo e recursos)
  - **W**: Won't have (Requisito que não será incluído nesta versão do projeto)
- Escala de esforço para implementação:
  - **XS**: Esforço mínimo, tarefa simples e rápida de implementar
  - **S**: Esforço pequeno, tarefa relativamente simples, mas que pode exigir algum tempo
  - **M**: Esforço médio, tarefa que requer um tempo considerável e pode envolver complexidade moderada
  - **L**: Esforço grande, tarefa complexa que requer um tempo significativo e pode envolver desafios técnicos
  - **XL**: Esforço muito grande, tarefa extremamente complexa que requer um tempo muito longo e pode envolver desafios técnicos significativos
  (Em ambiente de desenvolvimento Ágil, a classificação de esforço pode passar a ser feita utilizando pontos de história, para maior precisão e flexibilidade na estimativa de tarefas. Nesse caso, utilizar-se-á avaliação por método ***SCRUM POKER*** com escala ***Fibonacci adaptada*** -  0, 1, 2, 3, 5, 8, 13, 20, 40, 100)