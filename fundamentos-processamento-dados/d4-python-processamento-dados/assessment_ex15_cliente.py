# =====================================================================
# Assessment — notebook 2: Exercício 15
# Consome a rota GET /produtos-comuns criada no notebook 1 (assessment.py)
# Python para Processamento de Dados · Instituto Infnet
# =====================================================================

import requests
import json

url_base = "https://3105cfef-52de-48ae-84be-a268ddf29cb9.deepnoteproject.com/"

resposta = requests.get(url_base + "/produtos-comuns")
produtos = resposta.json()

print(f"Produtos em comun: {produtos}")
# Saída obtida: Produtos em comun: ['Fone', 'Mouse', 'Teclado']
