-- =====================================================================
-- TP1 — Modelagem de uma biblioteca (parte em SQL)
-- SQL e Modelagem Relacional · Instituto Infnet
-- Executado no Deepnote (DuckDB), lendo a planilha original biblioteca.csv.
-- As respostas escritas estão em tp1-modelagem-biblioteca.md
-- =====================================================================

-- Ex. 6 — Tabela livro, ainda sem restrições
DROP TABLE IF EXISTS livro;
CREATE TABLE livro (
    isbn TEXT,
    livro_titulo TEXT,
    autor TEXT,
    marcas_uso TEXT
);
INSERT INTO livro (isbn, livro_titulo, autor, marcas_uso)
SELECT DISTINCT isbn, livro_titulo, autor, marcas_uso
FROM read_csv_auto('/work/biblioteca.csv');
SELECT * FROM livro;

-- Ex. 7 — Tabela livro com restrições
DROP TABLE IF EXISTS livro;
CREATE TABLE livro (
    isbn TEXT NOT NULL UNIQUE,
    livro_titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    marcas_uso TEXT
);
INSERT INTO livro (isbn, livro_titulo, autor, marcas_uso)
SELECT DISTINCT isbn, livro_titulo, autor, marcas_uso
FROM read_csv_auto('/work/biblioteca.csv');
SELECT * FROM livro;

-- Ex. 9 — Tabela leitor, ainda sem restrições
DROP TABLE IF EXISTS leitor;
CREATE TABLE leitor (
    leitor_email TEXT,
    leitor_nome TEXT,
    leitor_curso TEXT,
    telefone_leitor TEXT,
    data_cadastro DATE
);
INSERT INTO leitor (leitor_email, leitor_nome, leitor_curso, telefone_leitor, data_cadastro)
SELECT DISTINCT leitor_email, leitor_nome, leitor_curso, telefone_leitor, data_cadastro
FROM read_csv_auto('/work/biblioteca.csv');
SELECT * FROM leitor;

-- Ex. 10 — Tabela leitor com restrições
DROP TABLE IF EXISTS leitor;
CREATE TABLE leitor (
    leitor_email TEXT NOT NULL UNIQUE,
    leitor_nome TEXT NOT NULL,
    leitor_curso TEXT NOT NULL,
    telefone_leitor TEXT,
    data_cadastro DATE NOT NULL
);
INSERT INTO leitor (leitor_email, leitor_nome, leitor_curso, telefone_leitor, data_cadastro)
SELECT DISTINCT leitor_email, leitor_nome, leitor_curso, telefone_leitor, data_cadastro
FROM read_csv_auto('/work/biblioteca.csv');
SELECT * FROM leitor;

-- Ex. 12 — Tabela emprestimo ligando livro e leitor
DROP TABLE IF EXISTS emprestimo;
CREATE TABLE emprestimo (
    isbn TEXT NOT NULL,
    leitor_email TEXT NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_limite DATE NOT NULL,
    data_devolucao DATE,
    FOREIGN KEY (isbn) REFERENCES livro(isbn),
    FOREIGN KEY (leitor_email) REFERENCES leitor(leitor_email)
);
INSERT INTO emprestimo (isbn, leitor_email, data_emprestimo, data_limite, data_devolucao)
SELECT isbn, leitor_email, data_emprestimo, data_limite, data_devolucao
FROM read_csv_auto('/work/biblioteca.csv');
SELECT * FROM emprestimo;

-- Ex. 13 — Empréstimo com identificador próprio (sequência)
DROP SEQUENCE IF EXISTS seq_emprestimo;
DROP TABLE IF EXISTS emprestimo;
CREATE SEQUENCE seq_emprestimo START 1;
CREATE TABLE emprestimo (
    id_emprestimo INTEGER DEFAULT nextval('seq_emprestimo') PRIMARY KEY,
    isbn TEXT NOT NULL,
    leitor_email TEXT NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_limite DATE NOT NULL,
    data_devolucao DATE,
    FOREIGN KEY (isbn) REFERENCES livro(isbn),
    FOREIGN KEY (leitor_email) REFERENCES leitor(leitor_email)
);
INSERT INTO emprestimo (isbn, leitor_email, data_emprestimo, data_limite, data_devolucao)
SELECT isbn, leitor_email, data_emprestimo, data_limite, data_devolucao
FROM read_csv_auto('/work/biblioteca.csv');
SELECT * FROM emprestimo;

-- Ex. 16 — Tabela de pendências para devoluções atrasadas
DROP TABLE IF EXISTS pendencia;
CREATE TABLE pendencia (
    id_pendencia INTEGER PRIMARY KEY,
    id_emprestimo INTEGER NOT NULL,
    data_registro DATE NOT NULL,
    valor_cobranca REAL NOT NULL,
    regularizada BOOLEAN NOT NULL,
    FOREIGN KEY (id_emprestimo) REFERENCES emprestimo(id_emprestimo)
);
SELECT * FROM pendencia;
