-- =====================================================================
-- TP2 — Normalização de uma loja virtual de artesanato
-- SQL e Modelagem Relacional · Instituto Infnet
-- Executado no Deepnote (DuckDB), lendo pedidos_artesanato.csv.
-- A análise escrita (ex. 1 a 5 e 16) está em tp2-normalizacao-loja.md
-- =====================================================================

-- Ex. 6 — Produtos extraídos da planilha (sem restrições)
DROP TABLE IF EXISTS produtos;
CREATE TABLE produtos AS
SELECT DISTINCT produto_nome, preco, peso_gramas
FROM read_csv_auto('pedidos_artesanato.csv');
SELECT * FROM produtos;

-- Ex. 7 — Produtos com chave e restrições
DROP TABLE IF EXISTS produtos;
CREATE TABLE produtos (
    produto_id INT PRIMARY KEY,
    produto_nome VARCHAR(100) NOT NULL UNIQUE,
    preco DECIMAL(10,2) NOT NULL,
    peso_gramas INT NOT NULL
);
INSERT INTO produtos
SELECT ROW_NUMBER() OVER (ORDER BY produto_nome) AS produto_id, produto_nome, preco, peso_gramas
FROM (
    SELECT DISTINCT produto_nome, preco, peso_gramas
    FROM read_csv_auto('pedidos_artesanato.csv')
);
SELECT * FROM produtos;

-- Ex. 8 — Endereços separados dos clientes (resolve a 3FN)
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS enderecos;
CREATE TABLE enderecos (
    cep VARCHAR(10) PRIMARY KEY,
    cidade VARCHAR(100) NOT NULL,
    estado CHAR(2) NOT NULL
);
CREATE TABLE clientes (
    cliente_id INTEGER PRIMARY KEY,
    cliente_nome VARCHAR(100) NOT NULL,
    cliente_email VARCHAR(100) NOT NULL UNIQUE,
    cliente_cpf VARCHAR(14) NOT NULL UNIQUE,
    cep VARCHAR(10) NOT NULL,
    FOREIGN KEY (cep) REFERENCES enderecos(cep)
);
INSERT INTO enderecos
SELECT DISTINCT cep, cidade_cliente, estado_cliente
FROM read_csv_auto('pedidos_artesanato.csv');
INSERT INTO clientes
SELECT ROW_NUMBER() OVER (ORDER BY cliente_cpf) AS cliente_id, cliente_nome, cliente_email, cliente_cpf, cep
FROM (
    SELECT DISTINCT cliente_nome, cliente_email, cliente_cpf, cep
    FROM read_csv_auto('pedidos_artesanato.csv')
);
SELECT * FROM enderecos;
SELECT * FROM clientes;

-- Ex. 9 — Pedidos ligados ao cliente
DROP TABLE IF EXISTS pedidos;
CREATE TABLE pedidos (
    pedido_id INTEGER PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    pedido_data DATE NOT NULL,
    status_pedido VARCHAR(20) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);
INSERT INTO pedidos
SELECT ROW_NUMBER() OVER (ORDER BY pedido_data) AS pedido_id, c.cliente_id, pedido_data, status_pedido
FROM (
    SELECT DISTINCT pedido_data, status_pedido, cliente_cpf
    FROM read_csv_auto('pedidos_artesanato.csv')
) p
JOIN clientes c ON c.cliente_cpf = p.cliente_cpf;
SELECT * FROM pedidos;

-- Ex. 10 — Itens do pedido (N:N pedido x produto)
DROP TABLE IF EXISTS pedido_itens;
CREATE TABLE pedido_itens (
    pedido_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    PRIMARY KEY (pedido_id, produto_id),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id)
);
INSERT INTO pedido_itens
SELECT DISTINCT p.pedido_id, pr.produto_id, quantidade
FROM read_csv_auto('pedidos_artesanato.csv') csv
JOIN pedidos p ON p.pedido_data = csv.pedido_data
JOIN produtos pr ON pr.produto_nome = csv.produto_nome;
SELECT * FROM pedido_itens;

-- Ex. 11 — Categorias separadas (resolve a 1FN)
DROP TABLE IF EXISTS produto_categoria;
DROP TABLE IF EXISTS categorias;
CREATE TABLE categorias (
    categoria_id INTEGER PRIMARY KEY,
    categoria_nome VARCHAR(100) NOT NULL UNIQUE
);
CREATE TABLE produto_categoria (
    produto_id INTEGER NOT NULL,
    categoria_id INTEGER NOT NULL,
    PRIMARY KEY (produto_id, categoria_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id),
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
);
INSERT INTO categorias
SELECT ROW_NUMBER() OVER (ORDER BY categoria_nome) AS categoria_id, categoria_nome
FROM (
    SELECT DISTINCT TRIM(UNNEST(STRING_SPLIT(categorias, ','))) AS categoria_nome
    FROM read_csv_auto('pedidos_artesanato.csv')
);
INSERT INTO produto_categoria
SELECT DISTINCT p.produto_id, c.categoria_id
FROM read_csv_auto('pedidos_artesanato.csv') csv
CROSS JOIN LATERAL (
    SELECT TRIM(UNNEST(STRING_SPLIT(csv.categorias, ','))) AS categoria_nome
) cat
JOIN produtos p ON p.produto_nome = csv.produto_nome
JOIN categorias c ON c.categoria_nome = cat.categoria_nome;
SELECT * FROM categorias;
SELECT * FROM produto_categoria;

-- Ex. 12 — Regras de negócio com CHECK (status permitido e quantidade positiva)
DROP TABLE IF EXISTS pedido_itens;
DROP TABLE IF EXISTS pedidos;
CREATE TABLE pedidos (
    pedido_id INTEGER PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    pedido_data DATE NOT NULL,
    status_pedido VARCHAR(20) NOT NULL CHECK (
        status_pedido IN ('pendente', 'em trânsito', 'entregue', 'cancelado')
    ),
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);
CREATE TABLE pedido_itens (
    pedido_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    PRIMARY KEY (pedido_id, produto_id),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id)
);
INSERT INTO pedidos
SELECT DISTINCT csv.pedido_id, c.cliente_id, csv.pedido_data, csv.status_pedido
FROM read_csv_auto('pedidos_artesanato.csv') csv
JOIN clientes c ON c.cliente_cpf = csv.cliente_cpf;
INSERT INTO pedido_itens
SELECT DISTINCT csv.pedido_id, p.produto_id, csv.quantidade
FROM read_csv_auto('pedidos_artesanato.csv') csv
JOIN produtos p ON p.produto_nome = csv.produto_nome;
SELECT * FROM pedidos;
SELECT * FROM pedido_itens;

-- Ex. 13 — Script completo do modelo + nova funcionalidade: avaliações de produtos
-- APAGA TUDO NA ORDEM CERTA
DROP TABLE IF EXISTS avaliacoes;
DROP TABLE IF EXISTS pedido_itens;
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS produto_categoria;
DROP TABLE IF EXISTS categorias;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS enderecos;
DROP TABLE IF EXISTS produtos;

-- CRIA
CREATE TABLE produtos (
    produto_id INT PRIMARY KEY,
    produto_nome VARCHAR(100) NOT NULL UNIQUE,
    preco DECIMAL(10,2) NOT NULL,
    peso_gramas INT NOT NULL
);
CREATE TABLE enderecos (
    cep VARCHAR(10) PRIMARY KEY,
    cidade_cliente VARCHAR(100) NOT NULL,
    estado_cliente CHAR(2) NOT NULL
);
CREATE TABLE clientes (
    cliente_id INT PRIMARY KEY,
    cliente_nome VARCHAR(100) NOT NULL,
    cliente_email VARCHAR(100) NOT NULL UNIQUE,
    cliente_cpf VARCHAR(14) NOT NULL UNIQUE,
    cep VARCHAR(10) NOT NULL,
    FOREIGN KEY (cep) REFERENCES enderecos(cep)
);
CREATE TABLE pedidos (
    pedido_id INT PRIMARY KEY,
    cliente_id INT NOT NULL,
    pedido_data DATE NOT NULL,
    status_pedido VARCHAR(20) NOT NULL CHECK (status_pedido IN ('pendente', 'em trânsito', 'entregue', 'cancelado')),
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);
CREATE TABLE pedido_itens (
    pedido_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL CHECK (quantidade > 0),
    PRIMARY KEY (pedido_id, produto_id),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id)
);
CREATE TABLE categorias (
    categoria_id INT PRIMARY KEY,
    categoria_nome VARCHAR(100) NOT NULL UNIQUE
);
CREATE TABLE produto_categoria (
    produto_id INT NOT NULL,
    categoria_id INT NOT NULL,
    PRIMARY KEY (produto_id, categoria_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id),
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
);
CREATE TABLE avaliacoes (
    avaliacao_id INT PRIMARY KEY,
    cliente_id INT NOT NULL,
    produto_id INT NOT NULL,
    nota INT NOT NULL CHECK (nota BETWEEN 1 AND 5),
    comentario VARCHAR(255),
    avaliacao_data DATE NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id)
);

-- INSERE
INSERT INTO enderecos
SELECT DISTINCT cep, cidade_cliente, estado_cliente
FROM read_csv_auto('pedidos_artesanato.csv');

INSERT INTO produtos
SELECT ROW_NUMBER() OVER (ORDER BY produto_nome) AS produto_id, produto_nome, preco, peso_gramas
FROM (SELECT DISTINCT produto_nome, preco, peso_gramas FROM read_csv_auto('pedidos_artesanato.csv'));

INSERT INTO clientes
SELECT ROW_NUMBER() OVER (ORDER BY cliente_cpf) AS cliente_id, cliente_nome, cliente_email, cliente_cpf, cep
FROM (SELECT DISTINCT cliente_nome, cliente_email, cliente_cpf, cep FROM read_csv_auto('pedidos_artesanato.csv'));

INSERT INTO pedidos
SELECT DISTINCT csv.pedido_id, c.cliente_id, csv.pedido_data, csv.status_pedido
FROM read_csv_auto('pedidos_artesanato.csv') csv
JOIN clientes c ON c.cliente_cpf = csv.cliente_cpf;

INSERT INTO pedido_itens
SELECT DISTINCT csv.pedido_id, p.produto_id, csv.quantidade
FROM read_csv_auto('pedidos_artesanato.csv') csv
JOIN produtos p ON p.produto_nome = csv.produto_nome;

INSERT INTO categorias
SELECT ROW_NUMBER() OVER (ORDER BY categoria_nome) AS categoria_id, categoria_nome
FROM (SELECT DISTINCT TRIM(UNNEST(STRING_SPLIT(categorias, ','))) AS categoria_nome FROM read_csv_auto('pedidos_artesanato.csv'));

INSERT INTO produto_categoria
SELECT DISTINCT p.produto_id, c.categoria_id
FROM read_csv_auto('pedidos_artesanato.csv') csv
CROSS JOIN LATERAL (SELECT TRIM(UNNEST(STRING_SPLIT(csv.categorias, ','))) AS categoria_nome) cat
JOIN produtos p ON p.produto_nome = csv.produto_nome
JOIN categorias c ON c.categoria_nome = cat.categoria_nome;

INSERT INTO avaliacoes
SELECT ROW_NUMBER() OVER (ORDER BY a.data_avaliacao) AS avaliacao_id, c.cliente_id, p.produto_id, a.nota, a.comentario, a.data_avaliacao
FROM read_csv_auto('avaliacoes_proposta_alternativa.csv') a
JOIN clientes c ON c.cliente_nome = a.cliente_nome
JOIN produtos p ON p.produto_nome = a.produto_nome;

SELECT * FROM pedido_itens;

-- Ex. 14 — Inserções manuais de teste
INSERT OR IGNORE INTO produtos (produto_id, produto_nome, preco, peso_gramas)
VALUES (1, 'Vaso de cerâmica', 89.90, 850);
INSERT OR IGNORE INTO produtos (produto_id, produto_nome, preco, peso_gramas)
VALUES (2, 'Bolsa de palha', 120.00, 320);
INSERT OR IGNORE INTO clientes (cliente_id, cliente_nome, cliente_email, cliente_cpf, cep)
VALUES (1, 'Ana Souza', 'ana@email.com', '111.111.111-11', '01310-100');
INSERT OR IGNORE INTO avaliacoes (avaliacao_id, cliente_id, produto_id, nota, comentario, avaliacao_data)
VALUES (1, 1, 1, 5, 'Produto muito bonito e bem acabado.', '2026-03-01');
SELECT * FROM avaliacoes;

-- Ex. 15 — Carga das avaliações a partir do CSV
INSERT INTO avaliacoes
SELECT ROW_NUMBER() OVER (ORDER BY a.data_avaliacao) AS avaliacao_id, c.cliente_id, p.produto_id, a.nota, a.comentario, a.data_avaliacao
FROM read_csv_auto('avaliacoes_proposta_alternativa.csv') a
JOIN clientes c ON c.cliente_nome = a.cliente_nome
JOIN produtos p ON p.produto_nome = a.produto_nome;
SELECT * FROM avaliacoes;

-- Ex. 16 — Correção da proposta alternativa de avaliações
-- (análise de 1FN, 2FN e 3FN em tp2-normalizacao-loja.md)
-- 1FN: categorias em tabela própria + tabela de ligação
CREATE TABLE categorias (
    categoria_id INT PRIMARY KEY,
    categoria_nome VARCHAR(100) NOT NULL UNIQUE
);
CREATE TABLE produto_categoria (
    produto_id INT NOT NULL,
    categoria_id INT NOT NULL,
    PRIMARY KEY (produto_id, categoria_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id),
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
);
-- 2FN: dados do produto separados
CREATE TABLE produtos (
    produto_id INT PRIMARY KEY,
    produto_nome VARCHAR(100) NOT NULL UNIQUE
);
-- 3FN: dados do cliente separados
CREATE TABLE clientes (
    cliente_id INT PRIMARY KEY,
    cliente_nome VARCHAR(100) NOT NULL,
    cliente_email VARCHAR(100) NOT NULL UNIQUE
);
-- Avaliação apenas com seus próprios dados e as chaves estrangeiras
CREATE TABLE avaliacoes (
    avaliacao_id INT PRIMARY KEY,
    cliente_id INT NOT NULL,
    produto_id INT NOT NULL,
    nota INT NOT NULL CHECK (nota BETWEEN 1 AND 5),
    comentario VARCHAR(255),
    data_avaliacao DATE NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id)
);
