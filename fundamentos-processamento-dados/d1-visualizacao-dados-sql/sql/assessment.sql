-- =====================================================================
-- Assessment — Introdução à Visualização de Dados e SQL (Infnet)
-- Parte 2: consultas SQL (exercícios 5 a 16)
-- Autor: Adryan da Silva Santos
-- =====================================================================

-- ---------------------------------------------------------------------
-- Tabela: filmes
-- ---------------------------------------------------------------------

-- Exercício 5 — Filmes disponíveis no catálogo
SELECT titulo, genero, classificacao
FROM filmes
WHERE disponivel_catalogo = 'SIM';

-- Exercício 6 — Mais de 90 min, nota abaixo de 8.5 e não indisponíveis
SELECT titulo, duracao_min, nota_media
FROM filmes
WHERE duracao_min > 90
  AND nota_media < 8.5
  AND disponivel_catalogo != 'NAO';

-- Exercício 7 — Gêneros estratégicos, da menor para a maior nota
SELECT titulo, genero, nota_media
FROM filmes
WHERE genero IN ('Ação', 'Drama', 'Ficção Científica')
ORDER BY nota_media ASC;

-- Exercício 8 — Resumo por gênero (só grupos com mais de um filme)
SELECT genero,
       COUNT(*)        AS quantidade_filmes,
       AVG(nota_media) AS nota_media,
       MIN(nota_media) AS menor_nota,
       MAX(nota_media) AS maior_nota
FROM filmes
WHERE disponivel_catalogo = 'SIM'
  AND duracao_min >= 80
  AND classificacao IN ('Livre', '12 anos')
GROUP BY genero
HAVING COUNT(*) > 1
ORDER BY AVG(nota_media) DESC;

-- ---------------------------------------------------------------------
-- Tabela: funcionarios
-- ---------------------------------------------------------------------

-- Exercício 9 — Funcionários ativos
SELECT nome_funcionario, cidade, estado
FROM funcionarios
WHERE status_ativo = 'SIM';

-- Exercício 10 — Ativos, +25 anos, salário > 4000, em SP/RJ/MG
SELECT nome_funcionario, salario, idade, estado
FROM funcionarios
WHERE idade > 25
  AND salario > 4000
  AND status_ativo = 'SIM'
  AND estado IN ('SP', 'RJ', 'MG')
ORDER BY idade DESC;

-- Exercício 11 — RJ/MG com salário > 3000, ou qualquer funcionário de SP
SELECT nome_funcionario, estado, salario
FROM funcionarios
WHERE (estado IN ('RJ', 'MG') AND salario > 3000)
   OR estado = 'SP'
ORDER BY estado DESC, nome_funcionario ASC;

-- Exercício 12 — Resumo por estado (só estados com mais de dois funcionários)
SELECT estado,
       COUNT(*)              AS total_funcionarios,
       COUNT(DISTINCT setor) AS total_setores,
       MIN(salario)          AS menor_salario,
       MAX(salario)          AS maior_salario
FROM funcionarios
WHERE status_ativo = 'SIM'
  AND idade >= 18
  AND estado IN ('SP', 'RJ', 'MG', 'PR')
GROUP BY estado
HAVING COUNT(*) > 2
ORDER BY COUNT(*) DESC;

-- ---------------------------------------------------------------------
-- Tabela: produtos_mercado
-- ---------------------------------------------------------------------

-- Exercício 13 — Produtos disponíveis para venda
SELECT *
FROM produtos_mercado
WHERE status_venda = 'Disponível';

-- Exercício 14 — Alimentos/Bebidas com estoque baixo, ou qualquer produto indisponível
-- (na base, "Alimentos" aparece dividido em Mercearia, Congelados, Laticínios,
--  Hortifruti e Padaria)
SELECT nome_produto, categoria, estoque, status_venda
FROM produtos_mercado
WHERE (categoria IN ('Mercearia', 'Congelados', 'Laticínios', 'Hortifruti', 'Padaria', 'Bebidas')
       AND estoque < 50)
   OR status_venda = 'Indisponível';

-- Exercício 15 — Disponíveis ou em promoção, do mais caro para o mais barato
SELECT nome_produto, preco, status_venda
FROM produtos_mercado
WHERE status_venda IN ('Disponível', 'Promoção')
ORDER BY preco DESC;

-- Exercício 16 — Resumo por categoria (só categorias com 3+ produtos)
SELECT categoria,
       COUNT(*)   AS quantidade_produtos,
       AVG(preco) AS preco_medio,
       SUM(preco) AS soma_precos,
       MIN(preco) AS menor_preco,
       MAX(preco) AS maior_preco
FROM produtos_mercado
WHERE preco >= 20
  AND estoque > 10
  AND status_venda IN ('Disponível', 'Promoção')
GROUP BY categoria
HAVING COUNT(*) >= 3
ORDER BY AVG(preco) DESC;
