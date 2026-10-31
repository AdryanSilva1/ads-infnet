-- =====================================================================
-- TP3 — Manipulação de dados (INSERT, UPDATE, DELETE, ALTER, TRUNCATE, DROP)
-- SQL e Modelagem Relacional · Instituto Infnet
-- Executado no Deepnote. As tabelas de cada sistema eram criadas por
-- células de setup fornecidas no enunciado.
-- =====================================================================

-- =====================================================================
-- SISTEMA A — Farmácia
-- Tabelas: medicamentos, fornecedores, lotes_estoque, promocoes_temporarias
-- =====================================================================

-- Ex. 1 — Cadastro de um novo medicamento
INSERT INTO medicamentos (id, nome, categoria, preco, fabricante)
VALUES (11, 'Dipirona Sódica 500mg', 'analgesicos', 12.90, 'LabVida');
SELECT * FROM medicamentos;

-- Ex. 2 — Remoção do fornecedor duplicado (somente o id 17)
DELETE FROM fornecedores WHERE id = 17;
SELECT * FROM fornecedores;

-- Ex. 3 — Nova coluna opcional de data de validade nos lotes
ALTER TABLE lotes_estoque ADD COLUMN data_validade DATE;

-- Ex. 4 — Reajuste de 5% apenas nos genéricos
UPDATE medicamentos SET preco = preco + (preco * 0.05) WHERE categoria = 'genericos';
SELECT * FROM medicamentos;

-- Ex. 5 — Lotes ativos vencidos passam a 'vencido' (data de hoje dinâmica)
UPDATE lotes_estoque SET status = 'vencido' WHERE status = 'ativo' AND CURRENT_DATE > data_validade;
SELECT * FROM lotes_estoque;

-- Ex. 6 — Esvaziar a tabela de promoções mantendo a estrutura
-- Uso TRUNCATE pois remove todos os dados mas mantém a estrutura da tabela,
-- permitindo que a próxima campanha seja inserida sem recriar nada.
-- O DROP TABLE seria inadequado pois removeria a tabela inteira do banco
-- e o DELETE é apropriado a remover linhas específicas com WHERE.
TRUNCATE promocoes_temporarias;
SELECT * FROM promocoes_temporarias;

-- Ex. 7 — Descontinuar a tabela de promoções
-- No Ex 6 usamos TRUNCATE pois a tabela continuaria sendo usada
-- na próxima campanha, apenas os dados precisavam ser removidos.
-- No Ex 7 usamos DROP TABLE pois a tabela não tem mais utilidade
-- no sistema e deve ser removida por completo do banco.
DROP TABLE promocoes_temporarias;

-- Ex. 8 — Reestruturação: nova tabela com princípio ativo obrigatório
CREATE TABLE medicamentos_v2 (
    id INTEGER,
    nome TEXT,
    categoria TEXT,
    preco REAL,
    fabricante TEXT,
    principio_ativo TEXT NOT NULL
);
INSERT INTO medicamentos_v2 (id, nome, categoria, preco, fabricante, principio_ativo)
SELECT id, nome, categoria, preco, fabricante, 'a definir' FROM medicamentos;
DROP TABLE medicamentos;
SELECT * FROM medicamentos_v2;

-- =====================================================================
-- SISTEMA B — Plataforma de podcasts
-- Tabelas: podcasts, episodios, inscricoes, recomendacoes_temporarias
-- =====================================================================

-- Ex. 9 — Cadastro de 4 episódios em uma única instrução
-- O enunciado indica id automático, porém o banco SQLite não possui
-- AUTO_INCREMENT configurado, exigindo o id manual para evitar erro
-- de NOT NULL. Por isso os ids foram definidos manualmente a partir do 293.
INSERT INTO episodios (id, podcast_id, titulo, data_lancamento, status)
VALUES (293, 12, 'Sons da Mata ao Amanhecer', '2026-04-10', 'publicado'),
       (294, 12, 'Encontro com os Ribeirinhos', '2026-04-17', 'publicado'),
       (295, 12, 'A Lenda do Boto-Cor-de-Rosa', '2026-04-24', 'rascunho'),
       (296, 12, 'O Silêncio da Floresta à Noite', '2026-05-01', 'rascunho');
SELECT * FROM episodios;

-- Ex. 10 — Correção pontual de título
UPDATE episodios SET titulo = 'Como começar na jardinagem' WHERE id = 287;
SELECT id, titulo FROM episodios;

-- Ex. 11 — Publicar rascunhos cuja data de lançamento já chegou
UPDATE episodios SET status = 'publicado' WHERE data_lancamento <= CURRENT_DATE AND status = 'rascunho';
SELECT titulo, data_lancamento, status FROM episodios;

-- Ex. 12 — Remover cancelamentos do 1º trimestre de 2025
DELETE FROM inscricoes
WHERE status = 'cancelada'
  AND strftime('%Y-%m', data_cancelamento) IN ('2025-01', '2025-02', '2025-03');
SELECT * FROM inscricoes;

-- Ex. 13 — Classificar podcasts por faixa de audiência
UPDATE podcasts SET faixa_audiencia = CASE
    WHEN total_reproducoes < 1000 THEN 'nicho'
    WHEN total_reproducoes > 1000 AND total_reproducoes <= 49999 THEN 'medio'
    WHEN total_reproducoes > 49999 THEN 'popular'
END;
SELECT titulo, total_reproducoes, faixa_audiencia FROM podcasts;

-- Ex. 14 — Retenção: contar antes de apagar (canceladas há mais de 2 anos)
SELECT COUNT(*) AS total_a_remover FROM inscricoes WHERE status = 'cancelada' AND data_cancelamento < '2024-06-02';
DELETE FROM inscricoes WHERE status = 'cancelada' AND data_cancelamento < '2024-06-02';

-- Ex. 15 — Fim de ciclo semanal x descontinuação
-- Cenário 1: usamos TRUNCATE pois limpa os dados e não mexe na estrutura da tabela,
-- permitindo que o job da semana seguinte insira normalmente.
-- Cenário 2: usamos DROP TABLE pois a tabela não tem mais função no banco,
-- removendo estrutura e dados de vez.
-- Cenário 1
TRUNCATE recomendacoes_temporarias;
-- Cenário 2
DROP TABLE recomendacoes_temporarias;

-- Ex. 16 — Rotina de manutenção trimestral
-- Etapa 1 (Inserção): INSERT pois estamos adicionando um novo registro ao catálogo.
INSERT INTO podcasts (id, titulo, categoria, total_reproducoes, faixa_audiencia)
VALUES (13, 'Cidades Invisíveis', 'urbanismo', 0, NULL);
SELECT * FROM podcasts;
-- Etapa 2 (Atualização): UPDATE pois estamos alterando o status de registros existentes.
UPDATE episodios SET status = 'arquivado' WHERE status = 'rascunho' AND data_lancamento < '2025-12-02';
SELECT * FROM episodios;
-- Etapa 3 (Remoção): DELETE pois estamos removendo registros que não têm mais utilidade no banco.
DELETE FROM inscricoes WHERE status = 'cancelada' AND data_cancelamento < '2023-06-02';
SELECT * FROM inscricoes;
