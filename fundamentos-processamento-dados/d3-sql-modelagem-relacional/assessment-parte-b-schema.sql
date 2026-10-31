-- =====================================================================
-- Assessment — Parte B: schema normalizado de um marketplace artesanal
-- SQL e Modelagem Relacional · Instituto Infnet
-- A análise (entidades, relacionamentos e normalização) está em
-- assessment-parte-b-modelagem.md
-- =====================================================================

-- Planilha original, importada para inspeção
CREATE OR REPLACE TABLE pedidos_planilha AS SELECT * FROM read_csv_auto('pedidos_planilha.csv');
SELECT * FROM pedidos_planilha;

-- Ex. 16 — CREATE TABLE do modelo final
CREATE TABLE cliente (
    cliente_id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    cidade TEXT
);

CREATE TABLE vendedor (
    vendedor_id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE conta_bancaria (
    conta_id INTEGER PRIMARY KEY,
    chave_pix TEXT NOT NULL,
    vendedor_id INTEGER UNIQUE REFERENCES vendedor(vendedor_id)  -- UNIQUE garante o 1:1
);

CREATE TABLE produto (
    produto_id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco_atual REAL NOT NULL,
    vendedor_id INTEGER NOT NULL REFERENCES vendedor(vendedor_id)
);

CREATE TABLE categoria (
    categoria_id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE pedido (
    pedido_id TEXT PRIMARY KEY,
    data TEXT NOT NULL,
    cliente_id INTEGER NOT NULL REFERENCES cliente(cliente_id)
);

CREATE TABLE item_pedido (
    item_id INTEGER PRIMARY KEY,
    pedido_id TEXT NOT NULL REFERENCES pedido(pedido_id),
    produto_id INTEGER NOT NULL REFERENCES produto(produto_id),
    quantidade INTEGER NOT NULL,
    preco_unitario REAL NOT NULL  -- preço cobrado no momento da compra
);

CREATE TABLE produto_categoria (
    produto_id INTEGER REFERENCES produto(produto_id),
    categoria_id INTEGER REFERENCES categoria(categoria_id),
    PRIMARY KEY (produto_id, categoria_id)
);

-- Ex. 16 — Dados da planilha no formato normalizado
INSERT INTO cliente VALUES
    (1, 'Marina Costa', 'marina@mail.com', 'São Paulo'),
    (2, 'Tiago Reis', 'tiago@mail.com', 'Curitiba'),
    (3, 'Larissa Veiga', 'lari@mail.com', 'Recife');

INSERT INTO vendedor VALUES
    (1, 'Atelier Lua', 'lua@atelier.com.br'),
    (2, 'Tecidos Nelm', 'nelm@tecidos.com.br'),
    (3, 'Madeira Viva', 'madv@artesa.com.br');

INSERT INTO conta_bancaria VALUES
    (1, 'lua-pix-01', 1),
    (2, 'nelm-pix-02', 2),
    (3, 'madv-pix-03', 3);

INSERT INTO produto VALUES
    (1, 'Vaso de cerâmica azul', 85.00, 1),
    (2, 'Almofada bordada flores', 45.00, 2),
    (3, 'Porta-copos rústico (kit 4)', 60.00, 3),
    (4, 'Tábua de queijo entalhada', 110.00, 3);

INSERT INTO categoria VALUES
    (1, 'decoração'),
    (2, 'cerâmica'),
    (3, 'casa'),
    (4, 'têxtil'),
    (5, 'madeira'),
    (6, 'cozinha');

INSERT INTO pedido VALUES
    ('P001', '2026-04-10', 1),
    ('P002', '2026-04-11', 2),
    ('P003', '2026-04-12', 1),
    ('P004', '2026-04-15', 3);

INSERT INTO item_pedido VALUES
    (1, 'P001', 1, 2, 85.00),
    (2, 'P001', 2, 1, 45.00),
    (3, 'P002', 1, 1, 85.00),
    (4, 'P003', 3, 1, 60.00),
    (5, 'P003', 2, 2, 45.00),
    (6, 'P004', 4, 1, 110.00);

INSERT INTO produto_categoria VALUES
    (1, 1), (1, 2),
    (2, 3), (2, 4), (2, 1),
    (3, 3), (3, 5),
    (4, 6), (4, 5);

-- Ex. 16 — Verificação: reconstrói as linhas da planilha a partir do modelo
SELECT
    p.pedido_id,
    c.nome AS cliente,
    pr.nome AS produto,
    ip.quantidade,
    ip.preco_unitario
FROM pedido p
JOIN cliente c ON p.cliente_id = c.cliente_id
JOIN item_pedido ip ON p.pedido_id = ip.pedido_id
JOIN produto pr ON ip.produto_id = pr.produto_id;
