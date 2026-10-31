# =====================================================================
# TP2 — Listas e dicionários
# Python para Processamento de Dados · Instituto Infnet
# Cada bloco era uma célula separada no Deepnote.
# =====================================================================


# --- Exercício 1 ---
produtos = input("Digite sua lista: ").split(',')

produtos_comuns = 0
produtos_destaque = 0

for i, produto in enumerate(produtos):
    if i % 2 != 0:
        print(f'{i+1}. {produto} [DESTAQUE]')
        produtos_destaque += 1
    else:
        print(f'{i+1}. {produto} [COMUM]')
        produtos_comuns += 1

print(f"Painel comum: {produtos_comuns} produto(s)")
print(f"Painel destaque: {produtos_destaque} produto(s)")


# --- Exercício 2 ---
fila = input("Digite a fila inicial: ").split(',')
atendimentos = 0

print(f"Fila inicial: {fila}")

while True:
    linha = input("Comando: ").strip()

    if linha.lower() == 'fim':
        break

    partes = linha.split()
    comando = partes[0].upper()

    if comando == 'ADICIONAR' and len(partes) > 1:
        fila.append(partes[1])
        print(f"'{partes[1]}' adicionado ao final da fila")

    elif comando == 'PRIORIDADE' and len(partes) > 1:
        fila.insert(0, partes[1])
        print(f"'{partes[1]}' inserido com PRIORIDADE no início.")

    elif comando == 'GRUPO' and len(partes) > 1:
        nomes = partes[1].split(',')
        fila.extend(nomes)
        print(f"Grupo {nomes} adicionado ao final")

    elif comando == 'CHAMAR':
        if fila:
            chamado = fila.pop(0)
            atendimentos += 1
            print(f"Chamando: '{chamado}' para atendimento!")
        else:
            print("A fila está vazia.")

    else:
        print(f"Comando inválido: '{linha}'.")

    print(f"Fila atual: {fila}\n")

print("=" * 50)
print("Sessão encerrada.")
print(f"Total de pacientes atendidos: {atendimentos}")
print("=" * 50)


# --- Exercício 3 ---
produtos = input("Digite os produtos: ").split(",")
precos = input("Digite seus respectivos preços: ").split(",")

precos_float = [float(p) for p in precos]

etiquetas = [
    f"Item {i+1:02}: {produto.strip()} | Original: R$ {preco:.2f} → Promocional: R$ {preco * 0.9:.2f}"
    for i, (produto, preco) in enumerate(zip(produtos, precos_float))
]

for etiqueta in etiquetas:
    print(etiqueta)

mais_barato = min(precos_float)
mais_caro = max(precos_float)
total_economizado = sum(p * 0.1 for p in precos_float)

print("--- Resumo ---")
print(f"Mais barato: {produtos[precos_float.index(mais_barato)].strip()} (R$ {mais_barato:.2f})")
print(f"Mais caro: {produtos[precos_float.index(mais_caro)].strip()} (R$ {mais_caro:.2f})")
print(f"Total economizado: R$ {total_economizado:.2f}")


# --- Exercício 4 ---
alunos = [
    ["Ana", 8.5],
    ["Bruno", 4.0],
    ["Carla", 6.0],
    ["Diego", 3.5],
    ["Elisa", 7.2],
    ["Fátima", 9.1]
]

# Relatório 1 - Aprovados (nota >= 6.0)
aprovados = [f"{nome} — {nota}" for nome, nota in alunos if nota >= 6.0]

# Relatório 2 - Conceitos (todos os alunos)
conceitos = [
    f"{nome} — {'Ótimo' if nota >= 8.0 else 'Bom' if nota >= 6.0 else 'Insuficiente'}"
    for nome, nota in alunos
]

print("--- Aprovados ---")
for a in aprovados:
    print(a)

print("--- Conceitos ---")
for c in conceitos:
    print(c)


# --- Exercício 5 ---
alunos = [
    ["Ana", 7.0, 8.5, 9.0],
    ["Bruno", 5.0, 6.0, 4.5],
    ["Carla", 8.0, 7.5, 9.5],
    ["Diego", 3.0, 4.0, 5.0],
    ["Elisa", 6.0, "sete", 8.0]
]

media_turma = 0
contador = 0
aprovados = 0
reprovados = 0

for aluno in alunos:

    nome = aluno[0]

    if type(aluno[1]) != str and type(aluno[2]) != str and type(aluno[3]) != str:

        media = (aluno[1] + aluno[2] + aluno[3]) / 3

        if media >= 6:
            situacao = "Aprovado"
            aprovados += 1
        else:
            situacao = "Reprovado"
            reprovados += 1

        print(f"{nome} — Média: {media:.1f} — {situacao}")

        media_turma += media
        contador += 1

    else:
        print(f"Registro inválido: {nome} (nota não numérica encontrada)")

print("--- Resumo da turma ---")

print(f"Média geral: {media_turma / contador:.1f}")

print(f"Aprovados: {aprovados} | Reprovados: {reprovados}")


# --- Exercício 6 ---
# Dicionário é ideal aqui pois permite associar cada palavra (chave)
# à sua contagem (valor), com busca e atualização em O(1).
# Com lista, precisaríamos percorrer tudo a cada contagem — muito menos eficiente.

texto = """O atendimento foi muito bom e o produto chegou rápido.
O produto estava com embalagem danificada, mas o atendimento resolveu rápido!
Muito satisfeito com o atendimento, produto excelente."""

# Remove pontuação
for caract in ".!?,":
    texto = texto.replace(caract, "")

# ✅ Nome diferente para a lista e para a variável do loop
palavras = texto.lower().split()

contagem = {}

for palavra in palavras:
    if len(palavra) > 3:
        contagem[palavra] = contagem.get(palavra, 0) + 1

ranking = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

for palavra, n in ranking:
    print(f"{palavra}: {n}")


# --- Exercício 7 ---
contatos_lista = [
    ["Ana", "11999990001", "ana@email.com"],
    ["Bruno", "11999990002", "bruno@email.com"],
    ["Ana", "11999990003", "ana.silva@email.com"],
    ["Carla", "11999990004", "carla@email.com"]
]

contatos_dict = {
    "Ana": [
        {"telefone": "11999990001", "email": "ana@email.com"},
        {"telefone": "11999990003", "email": "ana.silva@email.com"}
    ],
    "Bruno": [
        {"telefone": "11999990002", "email": "bruno@email.com"}
    ],
    "Carla": [
        {"telefone": "11999990004", "email": "carla@email.com"}
    ]
}

busca = input("Nome para buscar: ").capitalize()


print("\n--- BUSCANDO NA LISTA ---")
encontrado = False 
for contato in contatos_lista:
    if contato[0] == busca:
        print(f"Nome: {contato[0]} | Telefone: {contato[1]} | Email: {contato[2]}")
        encontrado = True
if not encontrado:
    print("Contato não encontrado.")


print("\n--- BUSCANDO NO DICIONÁRIO ---")
if busca in contatos_dict:
    for dados in contatos_dict[busca]:
        print(f"Nome: {busca} | Telefone: {dados['telefone']} | Email: {dados['email']}")
else:
    print("Contato não encontrado.")

# COMENTÁRIO OBRIGATÓRIO:
# O dicionário lida melhor com duplicatas. Na lista, é preciso percorrer
# todos os elementos e controlar manualmente uma variável (encontrado).
# No dicionário, o acesso é direto pela chave (nome), e as duplicatas já
# estão agrupadas numa lista de dicionários — o código fica mais curto,
# claro e sem risco de comparar campos errados (telefone ou email com o nome).


# --- Exercício 8 ---
produtos = [
    ("Caneta", 4.50),
    ("Mochila", 89.90),
    ("Tablet", 1200.00),
    ("Borracha", 2.00),
    ("Agenda", 65.00),
    ("Notebook", 3500.00),
    ("Lápis", 1.50),
    ("Monitor", 1800.00)
]

menor = min(p[1] for p in produtos)
maior = max(p[1] for p in produtos)
intervalo = (maior - menor) / 3

limite1 = menor + intervalo        
limite2 = menor + intervalo * 2   

catalogo = {
    "Baratos":        [],
    "Intermediários": [],
    "Caros":          []
}


for i, (nome, preco) in enumerate(produtos):
    if preco <= limite1:
        catalogo["Baratos"].append((nome, preco))
    elif preco <= limite2:
        catalogo["Intermediários"].append((nome, preco))
    else:
        catalogo["Caros"].append((nome, preco))

# Exibe as faixas calculadas
print("=== FAIXAS DE PREÇO ===")
print(f"Barato:        R$ {menor:.2f}  até R$ {limite1:.2f}")
print(f"Intermediário: R$ {limite1:.2f} até R$ {limite2:.2f}")
print(f"Caro:          R$ {limite2:.2f} até R$ {maior:.2f}")

# Relatório numerado por categoria
print("\n=== CATÁLOGO POR CATEGORIA ===")
for categoria, itens in catalogo.items():
    print(f"\n--- {categoria} ---")
    if not itens:
        print("  (nenhum produto nesta faixa)")
    else:
        for i, (nome, preco) in enumerate(itens, start=1):
            print(f"  {i}. {nome} — R$ {preco:.2f}")


# --- Exercício 9 ---
vendas = [
    ["Carlos", "Notebook", 2300.00],
    ["Beatriz", "Monitor", 899.00],
    ["Tiago", "Cabo HDMI", 45.00],
    ["Marina", "Teclado", 320.00],
    ["Lucas", "Webcam", 75.00],
    ["Fernanda", "SSD", 410.00]
]
meta = 500.00
minimo_permanencia = 100.00

acima_meta = [v for v in vendas if v[2] > meta]

print(f"=== Vendas acima da meta (R$ {meta:.2f}) ===")
for v in acima_meta:
    print(f"{v[0]} | {v[1]} | R$ {v[2]:.2f}")

for venda in vendas[:]:
    if venda[2] < minimo_permanencia:
        vendas.remove(venda)

print(f"\n=== Lista após remoção de vendas abaixo de R$ {minimo_permanencia:.2f} ===")
for v in vendas:
    print(v)


# --- Exercício 10 ---
turmas = [
    [8.0, 7.5, 9.0, 6.5],
    [5.0, 11.0, 7.0, 8.5, 6.0],
    [-1.0, 9.5, 8.0, 7.5],
    [10.0, 6.0, -3.0, 7.0, 15.0]
]

notas_validas = [nota for turma in turmas for nota in turma if 0 <= nota <= 10]

total_notas = sum(len(turma) for turma in turmas)
invalidas = total_notas - len(notas_validas)

media_global = sum(notas_validas) / len(notas_validas)

print("\n=== Exercício 10 ===")
print(f"Notas válidas: {notas_validas}")
print(f"Notas inválidas descartadas: {invalidas}")
print(f"Média global: {media_global:.2f}")

for i, turma in enumerate(turmas, start=1):
    validas_turma = [n for n in turma if 0 <= n <= 10]
    if validas_turma:
        media_turma = sum(validas_turma) / len(validas_turma)
        print(f"Média da turma {i}: {media_turma:.2f}")
    else:
        print(f"Turma {i}: nenhuma nota válida")

print(f"Maior nota: {max(notas_validas)}")
print(f"Menor nota: {min(notas_validas)}")


# --- Exercício 11 ---
estoque = {
    "Caneta azul": 15,
    "Papel A4": 500,
    "Borracha": 8,
    "Grampos": 3,
    "Caderno": 200,
    "Clips": 12,
    "Toner": 2,
    "Envelope": 45
}

# Dicionário é melhor que lista aqui pois permite acesso direto pelo nome
# do produto como chave, sem precisar percorrer todos os itens para encontrar um.

# Nível mínimo = média das quantidades dividida por 2.
# Justificativa: a média representa o "centro" do estoque atual.
# Dividir por 2 define um alerta para produtos bem abaixo da média,
# evitando alertas desnecessários para itens naturalmente escassos.
nivel_minimo = sum(estoque.values()) / len(estoque) / 2

abaixo = [produto for produto, qtd in estoque.items() if qtd < nivel_minimo]

alertas = []
for produto in abaixo:
    alertas.append((produto, estoque[produto]))

print(f"Nível mínimo sugerido: {nivel_minimo:.1f} unidades")
print("\n=== RELATÓRIO DE ALERTA ===")

if not alertas:
    print("Nenhum produto abaixo do nível mínimo.")
else:
    for i, (produto, qtd) in enumerate(alertas, start=1):
        print(f"{i}. {produto} — {qtd} unidades")


# --- Exercício 12 ---
invalidas = []
transacoes = []

while True:
    linha = input("Transação (ou fim): ")
    if linha == "fim":
        break

    partes = linha.split(",")

    if len(partes) != 3:
        invalidas.append(linha)
        continue

    tipo, descricao, valor_str = partes

    if tipo not in ("C", "D") or not descricao.strip():
        invalidas.append(linha)
        continue

    
    valor_limpo = valor_str.strip().replace(".", "", 1).replace("-", "", 1)
    if not valor_limpo.isdigit():
        invalidas.append(linha)
        continue

    valor = float(valor_str)
    transacoes.append((tipo, descricao.strip(), valor))


creditos = [(d, v) for tipo, d, v in transacoes if tipo == "C"]
debitos  = [(d, v) for tipo, d, v in transacoes if tipo == "D"]


resumo = {
    "total_creditos": sum(v for _, v in creditos),
    "total_debitos":  sum(v for _, v in debitos),
}
resumo["saldo"] = resumo["total_creditos"] - resumo["total_debitos"]
resumo["situacao"] = "Positivo" if resumo["saldo"] > 0 else "Negativo" if resumo["saldo"] < 0 else "Neutro"

print("\n=== Créditos ===")
for d, v in creditos:
    print(f"{d}: R$ {v:.2f}")
print(f"Total de créditos: R$ {resumo['total_creditos']:.2f}")

print("\n=== Débitos ===")
for d, v in debitos:
    print(f"{d}: R$ {v:.2f}")
print(f"Total de débitos: R$ {resumo['total_debitos']:.2f}")

print("\n=== Resumo ===")
print(f"Saldo final: R$ {resumo['saldo']:.2f}")
print(f"Situação: {resumo['situacao']}")

print(f"\n=== Linhas inválidas ({len(invalidas)}) ===")
for linha in invalidas:
    print(linha)


# --- Exercício 13 ---
modulos = ["Python Básico", "Estruturas de Dados", "Banco de Dados", "APIs"]
progresso = [
    ["Ana",    100, 85, 60, 90],
    ["Bruno",   70, 50, 40, 30],
    ["Carla",  100,100, 80, 95],
    ["Diego",   90, 75, 55, 70],
    ["Elisa",   60, 40, 30, 20],
    ["Fatima",  85, 90, 88, 92]
]

medias = []
for aluno in progresso:
    nome = aluno[0]
    total = aluno[1] + aluno[2] + aluno[3] + aluno[4]
    media = total / 4
    medias.append([nome, media])

for i in range(len(medias)):
    for j in range(i + 1, len(medias)):
        if medias[j][1] > medias[i][1]:
            medias[i], medias[j] = medias[j], medias[i]

print("\n=== Ranking de progresso ===")
for i, item in enumerate(medias, start=1):
    print(str(i) + ". " + item[0] + ": " + str(round(item[1], 1)) + "%")

# Critério de risco: média abaixo de 60% ou último módulo abaixo de 40%
# Justificativa: média < 60 indica desempenho geral fraco;
# último módulo < 40 detecta queda recente mesmo com média razoável.
em_risco = [aluno for aluno in progresso if (aluno[1]+aluno[2]+aluno[3]+aluno[4])/4 < 60 or aluno[4] < 40]

print("\n=== Alunos em risco (media < 60% ou ultimo modulo < 40%) ===")
for aluno in em_risco:
    media = (aluno[1]+aluno[2]+aluno[3]+aluno[4]) / 4
    print(aluno[0] + ": " + str(round(media, 1)) + "%")


# --- Exercício 14 ---
funcionarios = [
    {"nome": "Ana",    "departamento": "TI",     "salario": 6000.00, "anos": 5},
    {"nome": "Bruno",  "departamento": "Vendas", "salario": 3500.00, "anos": 1},
    {"nome": "Carla",  "departamento": "TI",     "salario": 7200.00, "anos": 8},
    {"nome": "Diego",  "departamento": "RH",     "salario": 4100.00, "anos": 2},
    {"nome": "Elisa",  "departamento": "Vendas", "salario": 3800.00, "anos": 4},
    {"nome": "Fátima", "departamento": "RH",     "salario": 4500.00, "anos": 6},
]
departamento_encerrado = input("Departamento a encerrar: ")


reajustados = [
    {**f, "salario_novo": round(f["salario"] * 1.15, 2), "reajuste": "15%"} if f["anos"] > 5
    else {**f, "salario_novo": round(f["salario"] * 1.12, 2), "reajuste": "12%"} if f["anos"] >= 3
    else {**f, "salario_novo": f["salario"], "reajuste": None}
    for f in funcionarios
]

print("\n=== Reajuste salarial ===")
for f in reajustados:
    if f["reajuste"]:
        print(f"{f['nome']} ({f['anos']} anos): R$ {f['salario']:.2f} → R$ {f['salario_novo']:.2f} ({f['reajuste']})")
    else:
        print(f"{f['nome']} ({f['anos']} ano(s)): sem reajuste")


print(f"\n=== Funcionários removidos (departamento encerrado: {departamento_encerrado}) ===")
for f in funcionarios[:]:
    if f["departamento"] == departamento_encerrado:
        print(f"{f['nome']} removido.")
        funcionarios.remove(f)

por_depto = {}
for f in funcionarios:
    depto = f["departamento"]
    if depto not in por_depto:
        por_depto[depto] = []
    por_depto[depto].append(f["nome"])

print("\n=== Funcionários remanescentes por departamento ===")
for depto, nomes in por_depto.items():
    print(depto + ":")
    for nome in nomes:
        print("  - " + nome)


# --- Exercício 15 ---
frota = [
    [101, "Centro",    40, 38, 40, 35, 39, 40],
    [202, "Aeroporto", 50, 20, 25, 18, 22, 30],
    [303, "Centro",    40, 36, 40, 40, 38, 37],
    [404, "Shopping",  30, 28, 30, 29, 27, 30],
    [505, "Aeroporto", 50, 45, 48, 50, 47, 49]
]

# Critério de reforço: taxa média >= 85%
# Justificativa: acima de 85% a linha opera perto do limite
# com frequência, indicando necessidade de mais veículos.

print("\n=== Taxa de ocupação por veículo ===")
for v in frota:
    t = round(sum(v[3:]) / len(v[3:]) / v[2] * 100, 1)
    print(f"Linha {v[0]} ({v[1]}): {t}%")

por_destino = {}
for v in frota:
    destino = v[1]
    if destino not in por_destino:
        por_destino[destino] = []
    por_destino[destino].append(v[0])

print("\n=== Linhas por destino ===")
for destino, linhas in por_destino.items():
    print(f"{destino}: {linhas}")

criticas = [
    [v[0], v[1], round(sum(v[3:]) / len(v[3:]) / v[2] * 100, 1)]
    for v in frota
    if round(sum(v[3:]) / len(v[3:]) / v[2] * 100, 1) >= 85
]

print("\n=== Linhas críticas (taxa >= 85%) ===")
for i, item in enumerate(criticas, start=1):
    print(f"{i}. Linha {item[0]} ({item[1]}): {item[2]}%")


# --- Exercício 16 ---
# Dicionário é melhor que listas paralelas pois mantém chave e valor
# juntos, sem risco de dessincronização entre listas separadas.

# Produtos com preços diferentes entre lojas: receita calculada por
# registro individual, preservando os dados reais de cada loja.

registros = []
while True:
    entrada = input("Registro (ou fim): ")
    if entrada == "fim":
        break
    partes = entrada.split(",")
    if len(partes) != 5:
        print("Linha inválida, ignorada.")
        continue

    loja      = partes[0]
    produto   = partes[1]
    categoria = partes[2]
    qtd_str   = partes[3].strip()
    preco_str = partes[4].strip()

    # Valida quantidade (inteiro)
    if not qtd_str.isdigit():
        print("Linha inválida, ignorada.")
        continue

    # Valida preço (número decimal)
    preco_limpo = preco_str.replace(".", "", 1)
    if not preco_limpo.isdigit():
        print("Linha inválida, ignorada.")
        continue

    registros.append([loja, produto, categoria, int(qtd_str), float(preco_str)])

meta_str = input("Meta de receita mínima por produto: ").strip()
meta_limpo = meta_str.replace(".", "", 1)
if not meta_limpo.isdigit():
    print("Meta inválida, usando 0.")
    meta = 0.0
else:
    meta = float(meta_str)

receita_cat     = {}
unidades_loja   = {}
receita_produto = {}

for r in registros:
    loja, produto, categoria, qtd, preco = r[0], r[1], r[2], r[3], r[4]
    receita = qtd * preco

    if categoria not in receita_cat:
        receita_cat[categoria] = []
    receita_cat[categoria].append(receita)

    if loja not in unidades_loja:
        unidades_loja[loja] = []
    unidades_loja[loja].append(qtd)

    if produto not in receita_produto:
        receita_produto[produto] = 0
    receita_produto[produto] += receita

print("\n=== Receita por categoria ===")
for cat in receita_cat:
    print(f"{cat}: R$ {sum(receita_cat[cat]):.2f}")

print("\n=== Unidades vendidas por loja ===")
for loja in unidades_loja:
    print(f"{loja}: {sum(unidades_loja[loja])} unidades")

maior_cat  = max(receita_cat,   key=lambda c: sum(receita_cat[c]))
maior_loja = max(unidades_loja, key=lambda l: sum(unidades_loja[l]))
print(f"\nCategoria com maior receita: {maior_cat}")
print(f"Loja com mais unidades: {maior_loja}")

abaixo_meta = [p for p in receita_produto if receita_produto[p] < meta]

print(f"\n=== Produtos abaixo da meta (R$ {meta:.2f}) ===")
for i, produto in enumerate(abaixo_meta, start=1):
    print(f"{i}. {produto}: R$ {receita_produto[produto]:.2f}")
