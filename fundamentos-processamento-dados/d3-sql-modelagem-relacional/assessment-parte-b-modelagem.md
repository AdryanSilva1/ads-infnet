# Assessment — Parte B: projeto de modelagem (marketplace artesanal)

Ponto de partida: uma planilha de pedidos com uma linha por item, dados de cliente e vendedor repetidos e várias categorias na mesma célula. O schema implementado está em [assessment-parte-b-schema.sql](assessment-parte-b-schema.sql).

## Ex. 13 — Reflexão e entidades

**Reflexão inicial:** um banco de dados relacional é apropriado porque permite organizar as informações em tabelas relacionadas, evitando a repetição de dados. Na planilha, clientes, vendedores e pedidos aparecem repetidas vezes, o que pode gerar inconsistências e dificultar atualizações. Outro problema está na coluna de categorias, que contém vários valores numa mesma célula, dificultando consultas e análises. Com um modelo relacional, cada informação é armazenada uma única vez e relacionada por chaves, o que melhora a organização, reduz erros e garante maior integridade dos dados.

**Entidades (8):**

| Entidade | Atributos | Por que é entidade própria |
|----------|-----------|----------------------------|
| Cliente | id, nome, email, cidade | pode realizar vários pedidos |
| Vendedor | id, nome, email | pode vender vários produtos |
| Conta bancária | id, chave_pix, vendedor_id | pertence exclusivamente a um vendedor |
| Produto | id, nome, preco_atual, vendedor_id | pertence a um vendedor e aparece em vários pedidos |
| Categoria | id, nome | padronizada e associada a vários produtos |
| Pedido | id, data, cliente_id | uma compra feita por um cliente |
| Item de pedido | id, pedido_id, produto_id, quantidade, preco_unitario | preserva o preço cobrado no momento da compra |
| Produto_categoria | produto_id, categoria_id | resolve o N:N entre produto e categoria |

## Ex. 14 — Relacionamentos e chaves

| Relação | Cardinalidade | Implementação |
|---------|:-------------:|---------------|
| Vendedor — Conta bancária | 1:1 | `vendedor_id` com `UNIQUE` em conta_bancaria |
| Vendedor → Produto | 1:N | `vendedor_id` em produto |
| Cliente → Pedido | 1:N | `cliente_id` em pedido |
| Pedido → Item de pedido | 1:N | `pedido_id` em item_pedido |
| Produto — Categoria | N:N | tabela de ligação produto_categoria |

O preço do momento da compra fica em `preco_unitario`, na tabela item_pedido.

## Ex. 15 — Normalização

- **1FN:** a coluna `categorias` guarda vários valores numa célula, separados por ponto e vírgula. No modelo, cada categoria fica na tabela categoria e se liga ao produto pela tabela produto_categoria.
- **2FN:** com uma chave composta (pedido_id + produto), atributos como `cliente`, `cli_email`, `cli_cidade`, `vendedor`, `vend_email` e `vend_pix` dependem só de parte da chave. No modelo, essas informações foram para entidades próprias.
- **3FN:** `vend_pix` depende do vendedor, e não do pedido ou do produto (dependência transitiva). O mesmo vale para `cli_cidade`, que depende do cliente. No modelo, esses atributos foram movidos para suas entidades.
