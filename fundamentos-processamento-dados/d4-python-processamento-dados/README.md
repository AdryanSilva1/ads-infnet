# 🐍 Python para Processamento de Dados

Disciplina 4 do bloco **Fundamentos do Processamento de Dados** — graduação em ADS Full Stack e Automação, Instituto Infnet (2º semestre de 2026).

**Ferramentas:** Python · Flask · requests · JSON · Deepnote

**Resultado:** ✅ Aprovado — **2 competências com DML e 3 com D**

---

## 🎯 Competências

| # | Competência | Conceito |
|---|-------------|:--------:|
| 1 | Manipular strings em Python | DML |
| 2 | Processar dados com listas e dicionários | D |
| 3 | Trabalhar com conjuntos, arquivos e JSON | D |
| 4 | Identificar e corrigir bugs em código Python | D |
| 5 | Consumir e expor dados por web services | DML |

## 📋 Entregas

| Atividade | Tema | Resultado | Entrega |
|-----------|------|:---------:|---------|
| TP1 | Manipulação de strings | 100% ✅ | 3h adiantado |
| TP2 | Listas e dicionários | 100% ✅ | 4 dias adiantado |
| TP3 | Conjuntos, arquivos e JSON | 100% ✅ | 4 dias adiantado |
| Assessment | Projeto integrando as 5 competências | 12/16 ⚠️ | 4 dias adiantado |

> No Assessment, os itens de 75% e 100% das competências 2, 3 e 4 não foram atingidos — as demais rubricas foram todas demonstradas.

---

## TP1 — Strings

Exercícios de limpeza, formatação e extração de informações de textos usando os métodos de string do Python.

💾 [Código](tp1_strings.py) · 🔗 [Notebook no Deepnote](https://deepnote.com/workspace/infnet-7b5bd4e4-8387-4b5e-b8b7-845a9c889146/project/acompanhar-aula-f20213c9-29c4-41d3-8cde-712e1dfc43b0/notebook/67fbc3508942450ea041ea64e26d1272)

## TP2 — Listas e dicionários

Processamento de coleções de dados: filtragem, agrupamento, contagem e transformação de registros com listas e dicionários.

💾 [Código](tp2_listas_dicionarios.py) · 🔗 [Notebook no Deepnote](https://deepnote.com/workspace/infnet-7b5bd4e4-8387-4b5e-b8b7-845a9c889146/project/Python-para-Processamento-de-Dados-TP2-ec65978d-7959-45f6-8dca-5a648c1ae014/notebook/Notebook-1-84ebec7843db42cb9e3d68f4f5929576)

## TP3 — Conjuntos, arquivos e JSON

Operações de conjunto (união, interseção, diferença), leitura e escrita de arquivos e serialização de dados em JSON.

💾 [Código](tp3_conjuntos_arquivos_json.py) · 🔗 [Notebook no Deepnote](https://deepnote.com/workspace/infnet-7b5bd4e4-8387-4b5e-b8b7-845a9c889146/project/DR4-TP3-Duplicate-534e7c36-e466-4072-a8c9-964703466fbd/notebook/tppythonbloco2competencia3-82d4daf6180642ea9d6e84ddbf7371f7)

## Assessment — projeto integrador

Exercícios cobrindo as cinco competências, incluindo:
- tratamento de strings e estruturas de dados
- leitura e gravação de arquivos JSON
- depuração de código com erros
- uma **API em Flask** com o endpoint `GET /produtos-comuns`
- um **cliente com `requests`** consumindo essa API
- uma chamada a um **modelo de IA via API (OpenRouter)**

> A chave da API de IA fica na variável de ambiente `OPENROUTER_API_KEY` e não está publicada neste repositório.

💾 [Código: ex. 1 a 14 e 16](assessment.py) · 💾 [Cliente da API: ex. 15](assessment_ex15_cliente.py) · 🔗 [Notebook no Deepnote](https://deepnote.com/workspace/infnet-7b5bd4e4-8387-4b5e-b8b7-845a9c889146/project/AT-DR-4-Duplicate-3105cfef-52de-48ae-84be-a268ddf29cb9/notebook/assessmentDR4-b762cc966e6946958cddd6db087a01bc)
