# =====================================================================
# TP3 — Conjuntos, arquivos e JSON
# Python para Processamento de Dados · Instituto Infnet
# Cada bloco era uma célula separada no Deepnote.
# =====================================================================


# --- Exercício 1 ---
acessos = ["ana", "bruno", "ana", "carla", "bruno", "diego"]
user_unico = 0
usuario = []
 
for c in acessos:
    if c not in usuario:
        user_unico += 1
        usuario.append(c)
 
usuario.sort()
print(f"{user_unico} usuários únicos")
print(", ".join(usuario))


# --- Exercício 2 ---
tag = []
total_tag = 0
while True:
    entrada = input("Digite a tag: ")
    if entrada == "fim":
        break
    if entrada not in tag:
        tag.append(entrada)
        total_tag += 1
 
tag.sort()
print(f"Total de tags: {total_tag}")
for t in tag:
    print(t)


# --- Exercício 3 ---
lista = set()  
while True:
    entrada = input("Digite o comando: ")
    if entrada == "sair":
        break
    if entrada.startswith("-"):
        nome_remov = entrada[1:]
        lista.discard(nome_remov)
    else:
        lista.add(entrada)
 
lista_ord = sorted(lista)
print(f"Presentes: {len(lista_ord)}")
print(", ".join(lista_ord))


# --- Exercício 4 ---
conteudo_acessos = """/home
/noticias/economia
/home
/esportes
/noticias/economia
/home
/sobre
/noticias/politica
/home
/noticias/economia
/esportes
/noticias/politica
/contato
/home
/noticias/tecnologia
/esportes
/home
/noticias/politica
/noticias/economia
/contato"""

with open("acessos.txt", "w", encoding="utf-8") as f:
    f.write(conteudo_acessos)

print("Arquivo acessos.txt criado.")


contagem = {}
with open("acessos.txt", "r") as arquivo:
    for linha in arquivo:
        url = linha.strip()
        if url in contagem:
            contagem[url] += 1
        else:
            contagem[url] = 1
 
for url, quantidade in contagem.items():
    print(f"{url}: {quantidade}")


# --- Exercício 5 ---
robotica = ["M001", "M002", "M003", "M005"]
programacao = ["M002", "M004", "M005", "M006"]

robotica_set = set(robotica)
programacao_set = set(programacao)

ambas_turmas = robotica_set.intersection(programacao_set)
apenas_prog = programacao_set.difference(robotica_set)
apenas_rob = robotica_set.difference(programacao_set)  
total_distintos = len(apenas_prog)+len(apenas_rob) + len(ambas_turmas)

print(f'Em ambos os cursos: {", ".join(sorted(ambas_turmas))}')
print(f'Apenas em Robótica: {", ".join(sorted(apenas_rob))}')        
print(f'Apenas em Programação: {", ".join(sorted(apenas_prog))}')
print(f"Total de alunos atendidos: {total_distintos}")


# --- Exercício 6 ---
emails = ["joao@empresa.com", "ana@gmail.com", "pedro@empresa.com", "ana@outlook.com"]
empresa = input("Digite a empresa: ")

total_encontrados = 0
encontrados = []

for email in emails:
    partes = email.split("@")

    if partes[1] == empresa:
        total_encontrados += 1
        encontrados.append(email)

print(f"Encontrados: {total_encontrados}")

for email in encontrados:
    print(email)


# --- Exercício 7 ---
conteudo_cardapio = """{
  "pizzas": [
    {"nome": "Margherita", "tamanho": "media", "preco": 42.90},
    {"nome": "Calabresa", "tamanho": "grande", "preco": 58.00},
    {"nome": "Quatro Queijos", "tamanho": "media", "preco": 49.50},
    {"nome": "Portuguesa", "tamanho": "grande", "preco": 65.00},
    {"nome": "Mussarela", "tamanho": "media", "preco": 39.00},
    {"nome": "Frango com Catupiry", "tamanho": "grande", "preco": 62.00},
    {"nome": "Vegetariana", "tamanho": "media", "preco": 45.50},
    {"nome": "Pepperoni", "tamanho": "grande", "preco": 69.90},
    {"nome": "Atum", "tamanho": "media", "preco": 51.00},
    {"nome": "Brócolis com Bacon", "tamanho": "grande", "preco": 67.50}
  ]
}"""

with open("cardapio.json", "w", encoding="utf-8") as f:
    f.write(conteudo_cardapio)

print("Arquivo cardapio.json criado.")


import json
 
with open("cardapio.json", "r") as cardapio:
    dados = json.load(cardapio)
 
orcamento_maximo = float(input("Digite seu orçamento máximo: "))
encontradas = []
 
for pizza in dados["pizzas"]:
    if pizza["preco"] <= orcamento_maximo:
        encontradas.append(pizza)
 
encontradas = sorted(encontradas, key=lambda pizza: pizza["preco"])
print(f"Pizzas dentro do orçamento: {len(encontradas)}")
for pizza in encontradas:
    print(f'{pizza["nome"]} ({pizza["tamanho"]}) - R$ {pizza["preco"]:.2f}')


# --- Exercício 8 ---
alunos = [("Ana", 8.5), ("Bruno", 6.0), ("Carla", 9.25)]
alunos = sorted(alunos, key=lambda aluno: aluno[0])
 
with open("boletim.txt", "w") as arquivo:
    for al, nt in alunos:
        arquivo.write(f"Aluno: {al} | Nota: {nt:.2f}\n")
 
print(f"Boletim gerado com {len(alunos)} alunos.")


# --- Exercício 9 ---
# O programa pode falhar porque o método remove() gera erro
# quando tenta remover um item que não está presente no conjunto.
# A lista de vendidos pode conter itens inexistentes no estoque
# ou itens repetidos, fazendo com que uma segunda tentativa de
# remoção seja realizada para um elemento que já foi removido.

disponiveis = {"caneta", "lapis", "borracha", "regua", "apontador"}
vendidos = ["caneta", "agenda", "regua", "estojo", "apontador", "caneta"]

for item in vendidos:
    disponiveis.discard(item)

print(disponiveis)


# --- Exercício 10 ---
palavras = ["dados", "limpos", "geram", "Dados", "claros", "ok", "limpos", "analise"]
palavras_distintas = []

for pl in palavras:
    if len(pl) >= 5:
        pl = pl.lower()
        palavras_distintas.append(pl)

palavras_distintas = set(palavras_distintas)
palavras_distintas = sorted(palavras_distintas)

print(f"Palavras longas distintas: {len(palavras_distintas)}")
for palavra in palavras_distintas:
    print(palavra)


# --- Exercício 11 ---
conteudo_vendas = """2025-03-01;monitor;1200.00
2025-03-01;mouse;45.50
2025-03-01;cabo HDMI;28.00
2025-03-02;notebook;3800.00
2025-03-02;cabo;15.00
2025-03-02;suporte para monitor;220.00
2025-03-03;teclado;180.00
2025-03-03;adaptador USB;35.90
2025-03-03;smartphone;2450.00
2025-03-04;fone bluetooth;320.00
2025-03-04;mousepad;25.00
2025-03-04;monitor ultrawide;2890.00
2025-03-05;webcam;480.00
2025-03-05;cabo de força;19.90
2025-03-05;tablet;1750.00
2025-03-06;impressora;890.00
2025-03-06;cartucho;120.00
2025-03-06;papel A4;42.00
2025-03-07;notebook gamer;5600.00
2025-03-07;mouse gamer;310.00"""

with open("vendas.txt", "w", encoding="utf-8") as f:
    f.write(conteudo_vendas)

print("Arquivo vendas.txt criado.")


vendas_altas = []

with open("vendas.txt", "r") as vendas:
    limite_minimo = float(input("Digite o limite mínimo de valor para que uma venda seja considerada de alto valor: "))

    for linha in vendas:
        dados = linha.split(";")

        if float(dados[2]) > limite_minimo:
            vendas_altas.append(linha)

with open("vendas_altas.txt", "w") as arquivo:
    for venda in vendas_altas:
        arquivo.write(venda)

print(f"{len(vendas_altas)} vendas filtradas.")


# --- Exercício 12 ---
conteudo_usuario = """{
  "nome": "Maria Silva",
  "email": "maria@email.com",
  "endereco": {
    "cidade": "Recife",
    "estado": "PE"
  },
  "pedidos": [
    {"id": 101, "valor": 250.00},
    {"id": 102, "valor": 89.90},
    {"id": 103, "valor": 1200.00},
    {"id": 104, "valor": 415.30},
    {"id": 105, "valor": 67.50}
  ]
}"""

with open("usuario.json", "w", encoding="utf-8") as f:
    f.write(conteudo_usuario)

print("Arquivo usuario.json criado.")


import json
 
with open("usuario.json", "r", encoding="utf-8") as f:
    usuario = json.load(f)
 
nome = usuario["nome"]
email = usuario["email"]
cidade = usuario["endereco"]["cidade"]
estado = usuario["endereco"]["estado"]
 
total_pedidos = 0
valor_total = 0.0
for pedido in usuario["pedidos"]:
    total_pedidos += 1
    valor_total += pedido["valor"]
 
print(f"Nome: {nome}")
print(f"Email: {email}")
print(f"Cidade/Estado: {cidade}/{estado}")
print(f"Total de pedidos: {total_pedidos}")
print(f"Valor total: R$ {valor_total:.2f}")


# --- Exercício 13 ---
conteudo_cadastros = """joao@empresa.com
  Maria@Empresa.com
ana@empresa.com
JOAO@empresa.com
  pedro@empresa.com  
maria@empresa.com
ana@empresa.com  
  Bruno@Empresa.com
felipe@empresa.com
PEDRO@empresa.com
  carla@empresa.com
Felipe@Empresa.com
bruno@empresa.com  
  lucas@empresa.com  
ana@EMPRESA.com"""

with open("cadastros.txt", "w", encoding="utf-8") as f:
    f.write(conteudo_cadastros)

print("Arquivo cadastros.txt criado.")


import json
 
emails_contagem = {}
 
with open("cadastros.txt", "r", encoding="utf-8") as f:
    for linha in f:
        email = linha.strip().lower()
        if email != "":
            if email in emails_contagem:
                emails_contagem[email] += 1
            else:
                emails_contagem[email] = 1
 
total_unicos = len(emails_contagem)
 
duplicados = []
for email in emails_contagem:
    if emails_contagem[email] > 1:
        duplicados.append(email)
duplicados.sort()
 
print(f"Total de e-mails únicos: {total_unicos}")
print("E-mails duplicados:")
if len(duplicados) == 0:
    print("Nenhum e-mail duplicado encontrado.")
else:
    for email in duplicados:
        print(email)


# --- Exercício 14 ---
import json
 
livros = []
for i in range(1, 4):
    print(f"--- Livro {i} ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano de publicação: "))
    generos_str = input("Gêneros (separados por vírgula): ")
 
    generos = []
    for g in generos_str.split(","):
        generos.append(g.strip())
 
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "generos": generos
    }
    livros.append(livro)
 
with open("biblioteca.json", "w", encoding="utf-8") as f:
    json.dump({"livros": livros}, f, ensure_ascii=False, indent=2)
 
print("Biblioteca cadastrada com 3 livros.")


# --- Exercício 15 ---
conteudo_pedidos = """{
  "pedidos": [
    {"id": 1, "cliente": "Ana", "status": "aberto", "total": 350.00},
    {"id": 2, "cliente": "Bruno", "status": "fechado", "total": 1200.00},
    {"id": 3, "cliente": "Carla", "status": "aberto", "total": 80.00},
    {"id": 4, "cliente": "Diego", "status": "aberto", "total": 990.00},
    {"id": 5, "cliente": "Eduarda", "status": "cancelado", "total": 540.00},
    {"id": 6, "cliente": "Felipe", "status": "aberto", "total": 2100.00},
    {"id": 7, "cliente": "Gabriela", "status": "fechado", "total": 175.00},
    {"id": 8, "cliente": "Henrique", "status": "aberto", "total": 410.00},
    {"id": 9, "cliente": "Isabela", "status": "aberto", "total": 65.00},
    {"id": 10, "cliente": "João", "status": "cancelado", "total": 880.00},
    {"id": 11, "cliente": "Karen", "status": "aberto", "total": 1530.00},
    {"id": 12, "cliente": "Lucas", "status": "fechado", "total": 720.00}
  ]
}"""

with open("pedidos.json", "w", encoding="utf-8") as f:
    f.write(conteudo_pedidos)

print("Arquivo pedidos.json criado.")


import json
 
with open("pedidos.json", "r", encoding="utf-8") as f:
    dados = json.load(f)
 
limite = float(input("Digite o limite mínimo de valor: "))
 
pendentes = []
for pedido in dados["pedidos"]:
    if pedido["status"] == "aberto" and pedido["total"] > limite:
        pendentes.append(pedido)
 
with open("pedidos_pendentes.json", "w", encoding="utf-8") as f:
    json.dump({"pendentes": pendentes}, f, ensure_ascii=False, indent=2)
 
print(f"{len(pendentes)} pedido(s) pendente(s) acima do limite.")


# --- Exercício 16 ---
conteudo_mensagens = """ana;bom dia pessoal
bruno;alguem viu o relatorio?
ana;eu vou enviar agora
carla;obrigada ana
ana;de nada
bruno;perfeito
daniel;cheguei atrasado, ja comecou?
ana;sim, mas ainda da tempo
bruno;qual a pauta de hoje?
carla;reuniao com o cliente as 14h
daniel;valeu carla
ana;alguem pode revisar o documento?
bruno;eu posso depois do almoco
elena;chegando agora, alguma novidade?
carla;tudo certo, elena
ana;elena, voce participa da reuniao?
elena;sim, claro
bruno;ate mais tarde entao
daniel;ate
ana;ate"""

with open("mensagens.txt", "w", encoding="utf-8") as f:
    f.write(conteudo_mensagens)

print("Arquivo mensagens.txt criado.")


import json
 
contagem = {}
 
with open("mensagens.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()
 
total_mensagens = len(linhas)
 
for linha in linhas:
    partes = linha.strip().split(";")
    remetente = partes[0]
    if remetente in contagem:
        contagem[remetente] += 1
    else:
        contagem[remetente] = 1
 
total_remetentes = len(contagem)
 
contagem_lista = []
for remetente in contagem:
    contagem_lista.append({"remetente": remetente, "mensagens": contagem[remetente]})
 
for i in range(len(contagem_lista)):
    for j in range(i + 1, len(contagem_lista)):
        a = contagem_lista[i]
        b = contagem_lista[j]
        if a["mensagens"] < b["mensagens"]:
            contagem_lista[i], contagem_lista[j] = b, a
        elif a["mensagens"] == b["mensagens"] and a["remetente"] > b["remetente"]:
            contagem_lista[i], contagem_lista[j] = b, a
 
relatorio = {
    "total_remetentes": total_remetentes,
    "total_mensagens": total_mensagens,
    "contagem": contagem_lista
}
 
with open("remetentes.json", "w", encoding="utf-8") as f:
    json.dump(relatorio, f, ensure_ascii=False, indent=2)
 
print(f"Relatório gerado com {total_remetentes} remetentes.")
