# =====================================================================
# Assessment — projeto integrador (notebook 1: exercícios 1 a 14 e 16)
# Python para Processamento de Dados · Instituto Infnet
# Cada bloco era uma célula separada no Deepnote.
# =====================================================================


# --- Exercício 1 ---
def rastreio(code):
    """Classifica cada código de rastreio e conta totais"""

    origem_nacional = 0
    destino_sp = 0

    for c in code:
        origem = c[0:2]
        numero = c[2:6]
        destino = c[6:8]

        if origem == "BR":
            origem_nacional += 1
        if destino == "SP":
            destino_sp +=1

        print(f"{c} -> Origem: {origem} | Numero :{numero} | Destino: {destino}")

    print(f"Encomendas de origem nacional: {origem_nacional}")
    print(f"Encomendas com destino SP: {destino_sp}")
      
    
    
codigos = "BR1023SP BR0987RJ IN4456SP BR2201MG IN0012RJ BR3345SP"
codigos = codigos.split(" ")
rastreio(codigos)


# --- Exercício 2 ---
def posicao(fila_inical):
    """Exibe fila enumerada a partir de 1"""
    pos=0
    for p in fila_inical:
        pos+=1
        print(f"{pos} - {p}")
    
def processar_remov_primeiros(fila_inical):
    """Remove os dois primeiros da fila"""
    nova_lista = fila_inical[2:]
    return nova_lista

def processar_prioridade(nova_lista,prioridade):
    """Adiciona a pessoa indicada como prioridade na primeira posição"""
    pedacos = prioridade.split("-")
    nome_cli = pedacos[1]
    nova_lista.insert(0,nome_cli)
    return nova_lista
    
def processar_nvs_clientes(nova_lista,novos_clientes):
    """Adiciona as novas pessoas ao final da fila"""
    nova_lista.extend(novos_clientes)
    return nova_lista


fila = ["Ana", "Diego", "Marcos", "Bia", "Rafa", "Tom"]
prioridade = "PRIORIDADE-Lucas"
novos_clientes = ["Bruno", "Carla"]

fila_remov = processar_remov_primeiros(fila)
nova_lista = processar_prioridade(fila_remov,prioridade)

print("===== FILA INICIAL =====")
posicao(fila)

print("===== FILA MODIFICADA =====")
fila_final = processar_nvs_clientes(nova_lista, novos_clientes)
posicao(fila_final)


# --- Exercício 3 ---
workshop_a = ["Ana", "Bruno", "Carla", "Ana", "Davi", "Bruno"]
workshop_b = ["Carla", "Edu", "Davi", "Carla", "Fabi"]
novo_a = ["Nina", "Luís"]
remover_b = ["Edu"]


set_a = set(workshop_a)
set_b = set(workshop_b)
total = set_a | set_b

print(f"Tamanho final de A: {len(total)}")

intersec = set_a & set_b 
print(f"Intersecção: {intersec}")

so_a = set_a - set_b
print(f"Apenas A: {so_a}")

set_a.update(novo_a)
print(f"A com as adições {set_a}")

set_b.discard(remover_b[0])
print(f"B após a remoção: {set_b}")


# --- Exercício 4 ---
# Escreva sua solução aqui
produtos = [
    ["Fone", 80.0, 5],
    ["Monitor", 150.0, 0],
    ["Teclado", 120.0, 3],
    ["Mouse", 45.0, 0],
    ["Cadeira", 220.0, 2],
]


disponiveis = [produto[0] for produto in produtos if produto[2] > 0]
print(f"Produtos disponiveis: {disponiveis}")

vitrine = {
    produto[0]: (produto[1] - (produto[1] * 0.10) if produto[1] > 100 else produto[1])
    for produto in produtos
    if produto[2] > 0
}
print(f"Produtos da vitrine: {vitrine}")


# --- Exercício 5 ---
def limpar_cadastro(linha):
    '''Limpa e separa nome, email e telefone de uma linha bruta'''
    partes = linha.split(";")

    nome = partes[0].strip()
    email = partes[1].strip()
    telefone_bruto = partes[2].strip()
    
    telefone = ""
    for c in telefone_bruto:
        if c.isdigit():
            telefone += c
    
    return (nome, email, telefone)


cadastro = """  Ana Souza ;ana@mail.com ; (11) 99999-8888
Bruno Lima;  bruno@mail.com;(21) 98888-7777  
 Carla Reis ; carla@mail.com ; (31) 3333-2211 """

linhas = cadastro.split("\n")

for linha in linhas:
    nome, email, telefone = limpar_cadastro(linha)
    print(f"Nome: {nome}| Email: {email} | Telefone: {telefone}")


# --- Exercício 6 ---
# Célula de preparação — cria um arquivo de exemplo para teste

conteudo = """Ana,22,backend
Bruno,17,frontend
Carla,30,backend
Davi,16,mobile
Edu,25,frontend
Fabi,19,backend"""

with open("inscricoes.txt", "w", encoding="utf-8") as f:
    f.write(conteudo)

print("inscricoes.txt criado.")



def separador(linha):
    """Separa uma linha bruta em nome, idade e categoria"""
    partes = linha.strip().split(",")
    nome = partes[0]
    idade = partes[1]
    categoria = partes[2]
    
    return nome,idade,categoria

def conversor(idade):
    """Converte a idadde de um texto para um numero int"""
    idade = int(idade)
    return(idade)



def processar_incricoes(nome_arquivo):
    """Lê o arquivo, filtra maiores de idade e retorna aprovados e estatísticas"""
    aprovados = []
    total_invalido = 0
    total_lido = 0

    with open(nome_arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    for linha in linhas:
        total_lido += 1
    
        try: 
            nome, idade, categoria = separador(linha)
            idade = conversor(idade)

            if idade >= 18:
                aprovados.append((nome, categoria))
            elif idade < 18:
                total_invalido += 1
                   
        except:
            total_invalido += 1
    
            

    return aprovados, total_lido, total_invalido

arquivo = "inscricoes.txt"
aprovados, total_lido, total_invalido = processar_incricoes(arquivo)

with open("aprovados.txt", "w", encoding="utf-8") as f:
    for nome,categoria in aprovados:
        f.write(f"{nome},{categoria}\n")

print("===== ESTASTISTICA =====")
print(f"Total de linhas lidas: {total_lido}")
print(f"Total de aprovados: {len(aprovados)}")
print(f"Total de linhas inválidas: {total_invalido}")

print("===== APROVADOS =====")
with open("aprovados.txt", "r", encoding="utf-8") as f:
    print(f.read())


# --- Exercício 7 ---
turma = [
    ["Ana", 7.0, 8.5, 6.0],
    ["Bruno", 9.0, 9.5, 8.0],
    ["Carla", 5.0, 6.0, 7.5],
    ["Davi", 8.0, 7.0, 9.0],
]

def media(notasturma):
    """Calcula a média de cada aluno, a média geral da turma e o aluno com maior média"""

    soma_geral = 0
    maior_media = 0
    nome_maior_media = ""
    
    print("===== MEDIA INDIVIDUAL =====")

    for n in notasturma:
        aluno = n[0]
        notas = n[1:]
        total_nota = 0
        quantos_valores = 0

        for nota in notas:
            total_nota = nota + total_nota
            quantos_valores += 1
    
        media_aluno = total_nota/quantos_valores

        if media_aluno > maior_media:
            maior_media = media_aluno
            nome_maior_media = aluno

        soma_geral = soma_geral + media_aluno
        
        print(f"O {aluno} teve uma média de {media_aluno:.1f}")

    media_geral = soma_geral / len(notasturma)
    print("==== MEDIA GERAL =====")
    print(f"A media geral da turma é {media_geral:.1f}")
    print("===== ALUNO DESTAQUE =====")
    print (f"A maior média é {maior_media:.1f} que pertence ao aluno {nome_maior_media}")

media(turma)


# Uma estrutura nome -> média faz mais sentido como dicionário,
# pois permite buscar a média de um aluno específico
# diretamente pelo nome (chave) sem precisar percorrer toda a
# estrutura como seria necessário em uma lista


# --- Exercício 8 ---
# Célula de preparação — cria um arquivo JSON de exemplo para teste

import json

pedidos = [
    {"cliente": "Ana", "itens": [{"produto": "Fone", "qtd": 2, "preco": 80.0},
                                  {"produto": "Mouse", "qtd": 1, "preco": 45.0}]},
    {"cliente": "Bruno", "itens": [{"produto": "Monitor", "qtd": 1, "preco": 150.0}]},
    {"cliente": "Ana", "itens": [{"produto": "Cadeira", "qtd": 1, "preco": 220.0}]},
    {"cliente": "Carla", "itens": [{"produto": "Teclado", "qtd": 3, "preco": 120.0}]},
]

with open("pedidos.json", "w", encoding="utf-8") as f:
    json.dump(pedidos, f)

print("pedidos.json criado.")


import json 
with open("pedidos.json", "r", encoding="utf-8") as f:
    pedidos = json.load(f)


def calcular_total_pedido(pedido):
    """Calcula o valor total de um pedido somando qtd * preco de cada item"""
    total = 0
    itens = pedido["itens"]
    
    for item in itens:
        qtd = item["qtd"]
        preco = item["preco"]
        total = total + (qtd * preco)
    
    return total

for p in pedidos:
    cliente = p["cliente"]
    total_pedido = calcular_total_pedido(p)
    print(cliente, total_pedido)


# --- Exercício 9 ---
# Célula de entrada de exemplo — código inicial com defeitos para depuração

alunos = {"Ana": [8, 9, 7], "Bruno": [], "Carla": [6, "x", 8]}
fila = ["10", "20", "abc", "30"]

# O Bruno tem lista de notas vazia o que causa zerodivisionerror
# ao dividir por len(notas) = 0. Corrigido com try/except ignorando o aluno sem dados válidos.
# A Carla tem uma nota em texto "x" o que causa typeerror ao tentar somar número com string,
# O mesmo try/except resolve.
# O while usava "i <= len(fila)" permitindo acessar um índice inexistente, corrigido para "i < len(fila)"
# A fila tem o valor "abc", que não pode ser convertido para inteiro corrigido com try/except, ignorando
#  esse valor e seguindo para o próximo.

for nome in alunos:
    try:
        notas = alunos[nome]
        media = sum(notas) / len(notas)
        print(nome, media)
    except:
        pass


i = 0
total = 0
while i < len(fila):
    try:
        total = total + int(fila[i])
    except:
        pass
    i = i + 1
print("Total da fila:", total)


# --- Exercício 10 ---
# Célula de preparação — cria um arquivo JSON de exemplo para teste

import json

vendas = [
    {"cliente": "Ana",   "produto": "Fone",    "qtd": 2, "mes": "2026-04"},
    {"cliente": "Bruno", "produto": "Monitor", "qtd": 1, "mes": "2026-04"},
    {"cliente": "Ana",   "produto": "Fone",    "qtd": 1, "mes": "2026-05"},
    {"cliente": "Carla", "produto": "Teclado", "qtd": 3, "mes": "2026-04"},
    {"cliente": "Ana",   "produto": "Mouse",   "qtd": 2, "mes": "2026-05"},
    {"cliente": "Bruno", "produto": "Fone",    "qtd": 1, "mes": "2026-05"},
    {"cliente": "Carla", "produto": "Fone",    "qtd": 2, "mes": "2026-05"},
]

with open("vendas.json", "w", encoding="utf-8") as f:
    json.dump(vendas, f)

print("vendas.json criado.")



import json 

try:    
    with open("vendas.json", "r", encoding="utf-8") as f:
        vendas = json.load(f)

except FileNotFoundError:
    print("O arquivo vendas.json não foi encontrado")

except:
    print("Não foi possível ler o arquivo")

def agrupamento(vendas):
    """Agrupa os dados da base"""
    base = {}
    for v in vendas:
        mes = v["mes"]
        produto = v["produto"]
        qtd = v["qtd"]

        if mes not in base:
            base[mes] = {}
            
        if produto not in base[mes]:
            base[mes][produto] = 0
        
        base[mes][produto] += qtd

    return base 

def mais_vendido(base):
    """Realiza a visualização do ranking do produto mais vendido e dos demais produtos que teve venda no mes """
    for mes in base:
        produtos_do_mes = base[mes]
        produto_mais_vendido = max(produtos_do_mes, key=produtos_do_mes.get)
        qtd_mais_vendido = produtos_do_mes[produto_mais_vendido]
        
        print(f"{mes} -> {produtos_do_mes} | mais vendido: {produto_mais_vendido} ({qtd_mais_vendido})") 

base = agrupamento(vendas)
mais_vendido(base)


# --- Exercício 11 ---
# Célula de preparação — cria um arquivo de log de exemplo para teste

log = """2026-05-20 09:01 | INFO  | ana    | login
2026-05-20 09:05 | ERROR | bruno  | falha de pagamento
2026-05-20 09:12 | WARN  | ana    | sessao expirando
2026-05-20 09:15 | ERROR | carla  | timeout na consulta
2026-05-20 09:20 | ERROR | bruno  | falha de pagamento
2026-05-20 09:33 | INFO  | bruno  | retry
2026-05-20 09:40 | ERROR | ana    | senha invalida
2026-05-20 09:55 | ERROR | carla  | timeout na consulta
2026-05-20 10:02 | WARN  | carla  | rate limit
2026-05-20 10:15 | ERROR | bruno  | falha de pagamento"""

with open("log.txt", "w", encoding="utf-8") as f:
    f.write(log)

print("log.txt criado.")


with open("log.txt", "r", encoding="utf-8") as f:
    log = f.readlines()


def detectar_incidentes(log):
    """Detecta dois ERROR consecutivos de um determinado user"""
    incidentes = []
    ultimo_nivel = {}

    for linha in log:
        partes = linha.split("|")
        timestamp = partes[0].strip()
        nivel = partes[1].strip()
        usuario = partes[2].strip()
        acao = partes[3].strip()
        
        if nivel == "ERROR":
            if usuario in ultimo_nivel and ultimo_nivel[usuario] == "ERROR":
                incidentes.append({"usuario": usuario, "timestamp": timestamp, "acao": acao})

        ultimo_nivel[usuario] = nivel
    
    return incidentes


incidentes = detectar_incidentes(log)

print("Incidentes detectados:")
for i in incidentes:
    usuario = i["usuario"]
    timestamp = i["timestamp"]
    acao = i["acao"]
    print(f"- {usuario} em {timestamp} ({acao})")

print(f"Total: {len(incidentes)}")


# --- Exercício 12 ---
cadastros = [
    {"nome": "Ana Silva",   "email": "ana@mail.com",     "telefone": "11999998888"},
    {"nome": "Bruno Lima",  "email": "bruno@mail.com",   "telefone": "(21) 98888-7777"},
    {"nome": "ANA",         "email": "ANA@MAIL.COM ",    "telefone": "11000001111"},
    {"nome": "Carla Reis",  "email": "carla@mail.com",   "telefone": "3133332211"},
    {"nome": "Bruno B.",    "email": "outro@mail.com",   "telefone": "21988887777"},
]


def limpeza_dados(cadastros):
    """Faz a limpeza dos dados e os guarda em variaveis indicadas """
    cadastros_unicos = []
    descartados = []
    emails_vistos = set()
    telefones_vistos = set()

    for c in cadastros:
        nome = c["nome"]
        email = c["email"].strip().lower()
        telefone_bruto = c["telefone"]
        telefone = ""

        for n in telefone_bruto:
            if n.isdigit():
                telefone = telefone + n

        if email in emails_vistos:
            descartados.append({"nome": nome, "motivo": "email duplicado"})

        elif telefone in telefones_vistos:
            descartados.append({"nome": nome, "motivo": "telefone duplicado"})

        else:
            cadastros_unicos.append({"nome":nome, "email":email,"telefone":telefone})
            emails_vistos.add(email)
            telefones_vistos.add(telefone)

    return cadastros_unicos, descartados

def mostrar(castro):
    """
    Serve pra realizar a visualização dos dados de maneira mais eficente e organizada funciona  
    tanto para os descartados e os sem duplicatas
    """

    for c in castro:
        if  "motivo" in c:
            nome = c["nome"]
            motivo = c["motivo"]
            print(f"Nome:{nome} (duplicado por {motivo}) ")
        else:
            nome = c["nome"]
            email = c["email"]
            telefone = c["telefone"]
            print(f"Nome:{nome} | Email: {email} | Telefone:{telefone}")
cadastros_unicos, descartados = limpeza_dados(cadastros)

print(f"Cadatros unicos: {len(cadastros_unicos)}")
print("==== Sem duplicatas ====")
mostrar(cadastros_unicos)
print(f"Cadatros descartados: {len(descartados)}")
print("==== Duplicados ====")
mostrar(descartados)


# Célula de instalação
# Execute uma vez no início da Parte B.

# pip install flask   (no Deepnote: !pip install flask)


# Célula inicial de preparação do Flask

import flask
import json

app = flask.Flask(__name__)

print("Flask preparado. O app foi criado.")


# --- Exercício 13 — 🛠️ Construção da rota `GET /produtos-comuns` ---
# Célula de preparação — define LOJA_A e LOJA_B em memória

LOJA_A = ["Fone", "Monitor", "Teclado", "Mouse", "Cadeira"]
LOJA_B = ["Teclado", "Mouse", "Webcam", "Mesa", "Fone"]

print("LOJA_A e LOJA_B definidas.")


def encontrar_comuns(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    comuns = set1 & set2
    return list(comuns)

@app.route("/produtos-comuns")
def produtos_comuns():
    resultado = encontrar_comuns(LOJA_A, LOJA_B)
    return json.dumps(resultado)


# --- Exercício 14 — Disponibilização do serviço Flask ---
# Sobe o servidor (no Deepnote ficava rodando numa célula; o Ex. 15 consome em outro notebook).
app.run(host="0.0.0.0", port=8080)


# --- Exercício 16 — Chamada simples a uma API de IA ---
# A chave fica numa variável de ambiente, nunca no código.
import os
import requests

chave_api = os.environ["OPENROUTER_API_KEY"]

url = "https://openrouter.ai/api/v1/chat/completions"

pergunta = "Explique em uma frase o que é uma API."

cabecalho = {
    "Authorization": "Bearer " + chave_api,
    "Content-Type": "application/json"
}

corpo = {
    "model": "openrouter/free",
    "messages": [
        {"role": "user", "content": pergunta}
    ]
}

resposta = requests.post(url, headers=cabecalho, json=corpo)

dados = resposta.json()
resposta_ia = dados["choices"][0]["message"]["content"]
print(dados)
print(resposta_ia)
