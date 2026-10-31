# 🐍 Introdução à Programação com Python

Disciplina 2 do bloco **Fundamentos do Processamento de Dados** — graduação em ADS Full Stack e Automação, Instituto Infnet (1º semestre de 2026).

**Ferramentas:** Python 3 · Deepnote · VS Code

**Resultado:** ✅ Aprovado — todas as competências demonstradas, 4 de 5 com o conceito máximo (DML)

---

## 🎯 Competências

| # | Competência | Conceito |
|---|-------------|:--------:|
| 1 | Criar programas simples em Python usando uma IDE "code playground" | DML |
| 2 | Criar programas simples com strings | D |
| 3 | Escrever programas simples com decisão / seleção em Python | DML |
| 4 | Escrever programas simples com repetição / iteração e listas em Python | DML |
| 5 | Programar funções personalizadas em Python | DML |

## 📋 Entregas

| Atividade | Tema | Resultado | Entrega |
|-----------|------|:---------:|---------|
| TP1 | Variáveis, tipos, operadores e fluxo IPO | 100% ✅ | 9 dias adiantado |
| TP2 | Strings, concatenação, `input()` e métodos de texto | 75% ⚠️ | 5 dias adiantado |
| TP3 | Condicionais, operadores lógicos e regras de negócio | 100% ✅ | 1 dia adiantado |
| Assessment | Funções, listas, repetição e algoritmos | 15 de 16 exercícios ✅ | 1 dia adiantado |

> Strings foi o ponto que ficou abaixo do máximo, no TP2 e no Assessment. Foi o que mais pratiquei depois, na disciplina seguinte (Python para Processamento de Dados).

---

## TP1 — Fundamentos

16 programas curtos sobre a base da linguagem:
- variáveis e tipos (`int`, `float`, `bool`, `str`) e `type()`
- operadores aritméticos, divisão inteira e módulo
- fluxo IPO (entrada → processamento → saída)

Os problemas simulam situações reais: carga máxima de um caminhão, ciclo de manutenção de uma planta, cálculo de imposto, conversão de minutos em horas e cálculo de folha de pagamento.

📄 [tp1.py](tp1.py)

## TP2 — Strings

Manipulação de texto em cenários de empresa:
- strings multilinha
- concatenação e repetição
- `upper()`, `lower()`, `capitalize()`, `swapcase()`, `count()` e `len()`
- leitura com `input()` e conversão de tipos

Exemplos: geração de SKU, montagem de URL de API, verificação de senha, limite de caracteres de SMS e log de transação formatado.

📄 [tp2.py](tp2.py)

## TP3 — Decisão e seleção

Estruturas `if` / `elif` / `else`, operadores lógicos e condicionais aninhadas aplicadas a regras de negócio:
- descontos progressivos de uma loja
- triagem de candidatos
- alerta meteorológico por nível de prioridade
- compatibilidade de doação de sangue
- cadastro KYC (PF/PJ)
- jogo de decisões encadeadas

📄 [tp3.py](tp3.py)

## Assessment — Consolidação

16 exercícios organizados em funções documentadas, juntando tudo o que foi visto:
- **Laços e listas:** contagem de pares e ímpares até "SAIR", soma e média de transações, interseção de listas, comparação de gabaritos
- **Validação:** algoritmo oficial de dígitos verificadores do CPF
- **Matemática aplicada:**
  - limite de uma função
  - velocidade quadro a quadro (derivada)
  - área sob uma curva (integral)
  - juros compostos com bônus e penalidade
  - estimativa de π pelo método de Monte Carlo
- **Jogo em modo texto:** movimentação de um personagem em um grid 20×20, com colisão nas bordas

📄 [assessment.py](assessment.py)

---

Cada exercício do Assessment está em uma função própria. Ao rodar `python assessment.py`, um menu deixa escolher qual exercício executar.
