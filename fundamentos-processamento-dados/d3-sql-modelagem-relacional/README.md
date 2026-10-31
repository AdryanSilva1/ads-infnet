# 🗄️ SQL e Modelagem Relacional

Disciplina 3 do bloco **Fundamentos do Processamento de Dados** — graduação em ADS Full Stack e Automação, Instituto Infnet (2º semestre de 2026).

**Ferramentas:** SQL (SQLite e DuckDB) · Deepnote

**Resultado:** ✅ Aprovado — **todas as competências demonstradas com o conceito DL**

---

## 🎯 Competências

| # | Competência | Conceito |
|---|-------------|:--------:|
| 1 | Projetar modelos relacionais de bases de dados com restrições, incluindo a criação das tabelas necessárias | DL |
| 2 | Aplicar regras de normalização em um modelo relacional de dados | DL |
| 3 | Manipular objetos em um banco de dados utilizando SQL | DL |
| 4 | Fazer agregações entre duas ou mais tabelas em banco de dados | DL |

## 📋 Entregas

| Atividade | Tema | Resultado | Entrega |
|-----------|------|:---------:|---------|
| TP1 | Modelagem de um sistema de biblioteca | 100% ✅ | 3h adiantado |
| TP2 | Normalização (1FN, 2FN e 3FN) de uma loja virtual | 100% ✅ | 7h após o prazo |
| TP3 | Manipulação de dados: INSERT, UPDATE, DELETE, ALTER, TRUNCATE/DROP | 100% ✅ | 1 dia adiantado |
| Assessment | JOINs, agregações e projeto completo de um marketplace | 100% em 3 competências; normalização em 75% ⚠️ | 1 dia adiantado |

> No Assessment, o único item que faltou foi o de 100% em normalização.

---

## TP1 — Modelagem de uma biblioteca

Ponto de partida: uma tabela única, montada por um estagiário, misturando livros, leitores e empréstimos, com dados repetidos e inconsistentes.

O que fiz:
- separei três entidades: **Livro**, **Leitor** e **Empréstimo** (o evento que liga os dois)
- defini os atributos e tipos de cada uma e escolhi os identificadores (ISBN e e-mail, com a ressalva de que o ISBN identifica a obra, não o exemplar)
- defini regras de negócio, como "um livro só pode ter um empréstimo ativo por vez"
- criei as tabelas em SQL, primeiro sem e depois com restrições (`NOT NULL`, `UNIQUE`, `PRIMARY KEY`)
- adicionei uma tabela de **pendências** para devoluções atrasadas, ligada ao empréstimo por chave estrangeira

📄 [Respostas escritas](tp1-modelagem-biblioteca.md) · 💾 [SQL](tp1-modelagem-biblioteca.sql) · 🔗 [Notebook no Deepnote](https://deepnote.com/workspace/infnet-7b5bd4e4-8387-4b5e-b8b7-845a9c889146/project/Adryan-da-Silva-Santoss-TP-1-75b97a42-8ef3-4d51-b7c4-d8a677c4d829/notebook/Notebook-1-418bed96074244a5801743a3819852ff)

## TP2 — Normalização de uma loja virtual

Uma planilha de pedidos com categorias empacotadas na mesma célula, dados de produto repetidos por pedido e endereço dependendo do CEP. Trabalhei:
- **diagnóstico** de cada violação: 1FN (categorias), 2FN (preço e peso dependendo só do produto) e 3FN (CEP → cidade → estado)
- **diagrama ER** do modelo proposto
- **implementação em SQL:** produtos, endereços, clientes, pedidos, itens do pedido e categorias com tabela de ligação
- **restrições de negócio** com `CHECK` (quantidade positiva e status permitido)
- **nova funcionalidade:** avaliações de produtos (N:N entre cliente e produto, nota de 1 a 5)

📄 [Análise e modelo](tp2-normalizacao-loja.md) · 💾 [SQL](tp2-normalizacao-loja.sql) · 🔗 [Projeto no Deepnote](https://deepnote.com/workspace/infnet-7b5bd4e4-8387-4b5e-b8b7-845a9c889146/project/Adryan-da-Silva-Santoss-Untitled-project-36b0dc1e-72a4-4494-a7e3-2d225ef7f9e8)

## TP3 — Manipulação de dados

16 operações em dois sistemas (uma farmácia e uma plataforma de podcasts):
- cadastros simples e em lote
- correções pontuais e atualizações em massa com `UPDATE ... WHERE`
- reajuste de preço e classificação com `CASE`
- datas dinâmicas para lotes vencidos e episódios pendentes
- política de retenção: contar antes de apagar
- evolução de estrutura com `ALTER TABLE` e reestruturação de tabela
- diferença prática entre esvaziar (`DELETE`) e eliminar (`DROP`) uma tabela

💾 [SQL](tp3-manipulacao-dados.sql) · 🔗 [Notebook no Deepnote](https://deepnote.com/workspace/infnet-7b5bd4e4-8387-4b5e-b8b7-845a9c889146/project/DR3-TP3-Duplicate-0079506d-46ca-4857-a885-03c0862d909d/notebook/tpsqlbloco2competencia3-5a684e4afd2f46aba54e469feba90190)

## Assessment — JOINs, agregações e projeto de modelagem

**Parte A — 12 consultas em dois bancos (biblioteca e liga de futebol), importados de CSV sem restrições:**
- criação de tabelas bem modeladas e migração dos dados crus
- `INNER JOIN`, `LEFT JOIN` com anti-join (livros nunca emprestados) e self-join (duplas do mesmo time)
- a mesma tabela usada três vezes com alias (time do jogador, mandante e visitante)
- saldo de gols com `CASE` dentro de agregações
- correção de uma query quebrada (`WHERE` com agregação em vez de `HAVING`, `GROUP BY` incompleto)

**Parte B — projeto completo de um marketplace artesanal:**
- análise de entidades e relacionamentos: 1:1 vendedor–conta, 1:N, e N:N produto–categoria
- preço preservado no item do pedido
- análise de 1FN, 2FN e 3FN na planilha original
- schema implementado com `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE` e `NOT NULL`
- dados migrados e uma query que reconstrói a planilha original sem perder informação

💾 [Parte A — queries](assessment-parte-a.sql) · 📄 [Parte B — modelagem](assessment-parte-b-modelagem.md) · 💾 [Parte B — schema](assessment-parte-b-schema.sql) · 🔗 [Notebook no Deepnote](https://deepnote.com/workspace/infnet-7b5bd4e4-8387-4b5e-b8b7-845a9c889146/project/assessmentDR3-Duplicate-0c623d81-8280-4e6a-ad9b-664f988157fd/notebook/assessmentDR3-7c23761063a94d419c53d6af23311206)
