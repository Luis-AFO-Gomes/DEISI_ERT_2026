# Requirements v0
Identificação inicial de requisitos

| Item | Requisito | Tipo<br>(F/nF/S) | Stakeholder | Prioridade<br><small>(MoSCoW)</small> | Esforço<br><small>(xs...XL)</small> | Variant?<br><small>(s/n)</small> |
|---:|---|---|---|---|---|---|
| 1 | O sistema deve apresentar a lista de títulos existente na página inicial | F | (anónimo) | M | XL | S |
| 2 | Ao seleccionar um título, deve ser apresentado os detalhes | F | (anónimo) | S | L | S |
| 3 | Ao apresentar os detalhes de um título, deve-se incluir o número de exemplares | F | (anónimo) | C | S | S |
| 4 | O sistema deve permitir que qualquer utilizador que lhe aceda se possa candidatar a sócio | F |Promotor | M | L | S |
| 5 | Um candidato só poderá ser aceite como sócio após validação por administrador da plataforma | F | Promotor | M | L | S |
| 6 | Qualquer sócio deverá poder adicionar títulos e exemplares à plataforma | F | Sócio<br>administrador | S | L | S |
| 7 | Caso o título adicionado já exista, deve-se manter o existente incrementando a contagem de exemplares | F | Administrador | C | S | S |
| 8 | A qualquer momento, o proprietario de um exemplar ou um administrador da plataforma podem retirar um exemplar de circulação | F | Sócio<br>Administrador | C | M | S |
| 9 | Exemplares retirados não são eliminados da plataforma para manutenção de histórico | F | Administrador | W | M | N |
| 10 | A plataforma será desenvolvida em Python com BD MySQL | S | N/A | N/A | N/A | N/A |
| ... | ... | ... | ... | ... | ... | ... |

## Ambiguity rewrite (min. 5)
1) **Item 10**<br>
   Original: "Desenvolvida em Python"
   Rewritten: "Nas versões iniciais, o desenvolvimento será efectuado em Python3, em linha de comando, para evitar a complexidade adicional da configuração de ambiente de produção"

2) **Item 9**<br>
   Original: "Exemplares retirados não são eliminados da plataforma"
   Rewritten: "O título continua a existir, mas terá a contagem de exemplares dos detalhes reduzida"
   Esta alteração não é relevante em contexto, só irá afectar a disponibilidade do título para empréstimos (funcionalidade de módulo que não faz parte da variante em desenvolvimento)