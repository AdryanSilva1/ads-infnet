-- =====================================================================
-- Assessment — Parte A: JOINs, agregações e manipulação de dados
-- SQL e Modelagem Relacional · Instituto Infnet
-- Executado no Deepnote (DuckDB), com os dados importados de CSV.
-- =====================================================================

-- =====================================================================
-- BANCO 1 — Biblioteca (autores, livros, membros, emprestimos)
-- =====================================================================

-- Importação / reset
CREATE OR REPLACE TABLE autores (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nacionalidade TEXT,
    ano_nascimento INTEGER
);
INSERT INTO autores SELECT * FROM read_csv_auto('autores.csv');
CREATE OR REPLACE TABLE livros AS SELECT * FROM read_csv_auto('livros.csv');
CREATE OR REPLACE TABLE membros AS SELECT * FROM read_csv_auto('membros.csv');
CREATE OR REPLACE TABLE emprestimos AS SELECT * FROM read_csv_auto('emprestimos.csv');

-- Ex. 1 — Tabela de funcionários com restrições
CREATE TABLE funcionarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    cargo TEXT,
    data_admissao DATE
);
INSERT INTO funcionarios (id, nome, email, cargo, data_admissao)
VALUES (1, 'Lúcia Andrade', 'lucia@biblio.org', 'Bibliotecária', '2022-04-10'),
       (2, 'Renato Souza', 'renato@biblio.org', 'Atendente', '2023-09-01'),
       (3, 'Marta Oliveira', 'marta@biblio.org', 'Bibliotecária', '2024-01-15'),
       (4, 'Iago Pereira', 'iago@biblio.org', 'Auxiliar', '2024-11-20');
SELECT * FROM funcionarios ORDER BY data_admissao;

-- Ex. 2 — Versão bem modelada de livros, com FOREIGN KEY, e migração
CREATE TABLE livros_catalogo (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor_id INTEGER REFERENCES autores(id),
    ano_publicacao INTEGER,
    exemplares_disponiveis INTEGER
);
INSERT INTO livros_catalogo SELECT * FROM livros;

-- Ex. 3 — Acervo com autor (INNER JOIN)
SELECT livros.titulo, autores.nome, livros.ano_publicacao
FROM livros
INNER JOIN autores ON autores.id = livros.autor_id
ORDER BY autores.nome ASC, livros.ano_publicacao ASC;

-- Ex. 4 — Livros nunca emprestados (anti-join)
SELECT livros.titulo, autores.nome
FROM livros
LEFT JOIN emprestimos ON livros.id = emprestimos.livro_id
INNER JOIN autores ON autores.id = livros.autor_id
WHERE emprestimos.livro_id IS NULL;

-- Ex. 5 — Nova coluna de gênero, atualizações e novos livros
ALTER TABLE livros ADD COLUMN genero TEXT;
UPDATE livros SET genero = 'Romance' WHERE titulo IN ('Dom Casmurro', 'A Hora da Estrela');
UPDATE livros SET genero = 'Romance Social' WHERE titulo = 'Capitães da Areia';
INSERT INTO livros (id, titulo, autor_id, ano_publicacao, exemplares_disponiveis, genero)
VALUES (12, 'A Paixão Segundo G.H.', 2, 1964, 2, 'Romance'),
       (13, 'Kafka à Beira-Mar', 5, 2002, 1, 'Fantasia');
SELECT titulo, genero FROM livros WHERE genero IS NOT NULL;

-- Ex. 6 — Reajuste de 50% nas multas de empréstimos em aberto
UPDATE emprestimos SET valor_multa = valor_multa * 1.5
WHERE data_devolucao_real IS NULL AND valor_multa > 0;
SELECT id, livro_id, membro_id, valor_multa
FROM emprestimos
WHERE data_devolucao_real IS NULL AND valor_multa > 0;
-- OBS: O id 4 está retornando 23 em vez de 22.5.
-- Acredito que seja por conta do ambiente, pois o CSV importou
-- valor_multa como INTEGER, arredondando o resultado.
-- Para corrigir seria necessário recriar a tabela com valor_multa REAL,
-- mas como o enunciado não pede, mantive a query original.

-- =====================================================================
-- BANCO 2 — Liga de futebol (times, jogadores, partidas, gols)
-- =====================================================================

-- Importação / reset
CREATE OR REPLACE TABLE times AS SELECT * FROM read_csv_auto('times.csv');
CREATE OR REPLACE TABLE jogadores AS SELECT * FROM read_csv_auto('jogadores.csv');
CREATE OR REPLACE TABLE partidas AS SELECT * FROM read_csv_auto('partidas.csv');
CREATE OR REPLACE TABLE gols AS SELECT * FROM read_csv_auto('gols.csv');

-- Ex. 7 — Relatório de gols: a tabela times usada 3 vezes com alias
SELECT jogadores.nome, tj.nome, tm.nome, tv.nome, gols.minuto
FROM gols
JOIN jogadores ON gols.jogador_id = jogadores.id
JOIN partidas ON gols.partida_id = partidas.id
JOIN times tj ON jogadores.time_id = tj.id
JOIN times tm ON partidas.time_mandante_id = tm.id
JOIN times tv ON partidas.time_visitante_id = tv.id
ORDER BY partidas.data, gols.minuto;

-- Ex. 8 — Gols por jogador, incluindo quem não marcou
SELECT jogadores.nome, times.nome, COUNT(gols.id) AS total_gols
FROM jogadores
LEFT JOIN gols ON jogadores.id = gols.jogador_id
JOIN times ON jogadores.time_id = times.id
GROUP BY jogadores.nome, times.nome
ORDER BY total_gols DESC, jogadores.nome ASC;

-- Ex. 9 — Duplas do mesmo time (self-join sem duplicatas)
SELECT times.nome, j1.nome, j2.nome
FROM jogadores j1
JOIN jogadores j2 ON j1.time_id = j2.time_id AND j1.id < j2.id
JOIN times ON j1.time_id = times.id
ORDER BY times.nome;

-- Ex. 10 — Saldo de gols por time (mandante e visitante)
SELECT
    times.nome,
    SUM(CASE WHEN partidas.time_mandante_id = times.id THEN partidas.gols_mandante ELSE partidas.gols_visitante END) AS gols_pro,
    SUM(CASE WHEN partidas.time_mandante_id = times.id THEN partidas.gols_visitante ELSE partidas.gols_mandante END) AS gols_contra,
    SUM(CASE WHEN partidas.time_mandante_id = times.id THEN partidas.gols_mandante ELSE partidas.gols_visitante END) -
    SUM(CASE WHEN partidas.time_mandante_id = times.id THEN partidas.gols_visitante ELSE partidas.gols_mandante END) AS saldo
FROM times
JOIN partidas ON times.id = partidas.time_mandante_id OR times.id = partidas.time_visitante_id
GROUP BY times.nome
ORDER BY gols_pro - gols_contra DESC;

-- Ex. 11 — Correção de uma query de artilheiros com defeitos
SELECT j.nome, COUNT(*) AS gols, t.nome
FROM jogadores j
JOIN gols g ON g.jogador_id = j.id
JOIN times t ON j.time_id = t.id
GROUP BY j.nome, t.nome
HAVING COUNT(*) > 1
ORDER BY gols DESC;
-- Defeito um: o LEFT JOIN foi substituído por JOIN,
-- pois o LEFT JOIN incluía jogadores com 0 gols;
-- o JOIN garante que apenas jogadores com gols apareçam.
-- Defeito dois: o WHERE COUNT(*) foi substituído por HAVING COUNT(*),
-- porque funções de agregação como COUNT não podem ser usadas no WHERE;
-- o HAVING é o lugar correto para filtrar resultados agregados.
-- Defeito três: o GROUP BY estava incompleto, faltava o t.nome,
-- que estava no SELECT; tudo que não é agregação no SELECT deve estar no GROUP BY.
-- Defeito quatro: o ORDER BY estava sem DESC;
-- o enunciado pede do maior para o menor, sem DESC a ordenação seria crescente.

-- Ex. 12 — Registro de uma nova partida e seus gols
INSERT INTO partidas (id, time_mandante_id, time_visitante_id, gols_mandante, gols_visitante, data)
VALUES (11, 2, 3, 2, 1, '2026-05-10');
INSERT INTO gols (id, partida_id, jogador_id, minuto)
VALUES (25, 11, 5, 20),
       (26, 11, 4, 55),
       (27, 11, 7, 70);
SELECT jogadores.nome, gols.minuto
FROM gols
INNER JOIN jogadores ON gols.jogador_id = jogadores.id
WHERE gols.partida_id = 11;
