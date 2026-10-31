# =====================================================================
# TP1 — Manipulação de strings
# Python para Processamento de Dados · Instituto Infnet
# Cada exercício era uma célula separada no Deepnote.
# =====================================================================

# Exercício 1 — Remover espaços do início e do fim de um e-mail
email = input("digite seu e-mail: ").strip()
print(f"Seu e-mail sem espaço no inicio e fim:{email}")


# Exercício 2 — Mensagem de agradecimento formatada
nome_completo = input("Digite o nome completo: ")
valor_compra = float(input("Digite o valor da compra: "))

print(f'{nome_completo} agradecemos sua compra no valor de R${valor_compra:.2f}.')


# Exercício 3 — Separar um registro de cliente em campos
registros_clientes = input("Digite o resgistro dos clientes: ")
registros = registros_clientes.split(";")

print(len(registros))
print(registros[0])  # nome
print(registros[1])  # cidade
print(registros[2])  # idade


# Exercício 4 — Montar um código de lote com join
centro_distribuicao = input("Digite o centro de distribuição: ")
categoria_produto = input("Digite a categoria do produto: ")
numero_lote = input("Digite o número do lote: ")

codigo_completo = '-'.join([centro_distribuicao, categoria_produto, numero_lote])

print(codigo_completo)


# Exercício 5 — Extrair partes de um código de crachá (fatiamento)
cod_cracha = input("Digite o codigo do cracha: ")

caracteres_alfanumericos = cod_cracha[4:10]
setor = cod_cracha[11:14]
turno = cod_cracha[-1]

print(f"O código interno do funcionario: {caracteres_alfanumericos}")
print(f"O setor do funcionario: {setor}")

if turno.upper() == 'M':
    print("Manha")
elif turno.upper() == 'T':
    print("Tarde")
elif turno.upper() == 'N':
    print("Noite")
else:
    print("Turno Invalido")


# Exercício 6 — Limpar e reformatar uma linha de relatório
relatorio = input("Digite a linha do relatório: ")
campos = relatorio.split(";")

lst_spc = []
for dados in campos:
    lst_spc.append(dados.strip())

resultado = ""
for i in range(len(lst_spc)):
    if i == len(lst_spc) - 1:
        resultado = resultado + lst_spc[i]
    else:
        resultado = resultado + lst_spc[i] + "/"

print(resultado)


# Exercício 7 — Validar prefixo e extensão de um arquivo
nome_arquivo = input("Digite o nome do arquivo: ")
prefixo = input("Digite o prefixo do departamento: ")

prefixo_valido = nome_arquivo.startswith(prefixo)
extensao_valida = nome_arquivo.endswith(".py") or nome_arquivo.endswith(".txt")

if prefixo_valido and extensao_valida:
    print("VÁLIDO")
elif not prefixo_valido and not extensao_valida:
    print("INVÁLIDO: prefixo e extensão incorretos")
elif not prefixo_valido:
    print("INVÁLIDO: prefixo incorreto")
else:
    print("INVÁLIDO: extensão incorreta")


# Exercício 8 — Decodificar um comando de 8 caracteres
dados = input("Digite os 8 caracteres: ")

coordenada = "X=" + dados[0] + ",Y=" + dados[1]
acao = dados[2:5]
tipo = dados[5]
defesa = dados[6]
atraso = dados[7]

print(f"Coordenada: {coordenada}")
print(f"Ação: {acao}")

if tipo.upper() == "A":
    print("Ataque")
elif tipo.upper() == "E":
    print("Especial")
else:
    print("Comum")

if defesa.upper() == "D":
    print("Defensivo")
elif atraso.upper() == "S":
    print("Com atraso")
else:
    print("Normal")


# Exercício 9 — Censurar palavras ofensivas
ofensas = ['bobo', 'chato', 'idiota', 'feio']
asteriscos = [' **** ', ' ***** ', ' ****** ', ' **** ']

mensagem = input("Digite a sua mensagem: ")

for i in range(len(ofensas)):
    mensagem = mensagem.replace(ofensas[i], asteriscos[i])

print(mensagem)


# Exercício 10 — Demonstrativo de fechamento de caixa alinhado
total_vendas = float(input("Digite o total das vendas brutas do dia: "))
custo_total = float(input("Digite o custo total dos produtos vendidos: "))
valor_despesas = float(input("Digite o valor total das despesas operacionais diversas: "))

receita_total = total_vendas - custo_total
saldo_final = receita_total - valor_despesas

if saldo_final > 0:
    status = "Positivo"
elif saldo_final < 0:
    status = "Negativo"
else:
    status = ""

print(f"Demonstrativo de Fechamento de Caixa")
print(f"{'Receita Total:':<20}{receita_total:>15.2f}")
print(f"{'Total de Despesas:':<20}{valor_despesas:>15.2f}")
print(f"{'Saldo Final:':<20}{saldo_final:>15.2f} {status}")


# Exercício 11 — Localizar um códon numa sequência de DNA
dna = input("Digite a sequência de DNA: ").upper()
codon = input("Digite o códon que se deseja localizar: ").upper()

posicao = dna.find(codon)

if posicao != -1:
    print("Encontrou na posição:", posicao)
else:
    print("-1")


# Exercício 12 — Trocar o separador de uma lista de nomes
nomes = input("Digite os nomes: ").split(",")

nome_div_barras = '/'.join(nomes)

print(nome_div_barras)


# Exercício 13 — Normalizar um endereço IPv4 digitado de forma irregular
ipv4 = input("Digite seu IPv4: ")

ipv4 = ipv4.replace("-", ".")
ipv4 = ipv4.replace("_", ".")
ipv4 = ipv4.split(".mask")[0]
octetos = ipv4.split(".")

resultado = []

for octeto in octetos:

    if octeto.isdigit() and 0 <= int(octeto) <= 255:
        resultado.append(octeto)

    else:
        resultado.append("0")

while len(resultado) < 4:
    resultado.append("0")

print("{}.{}.{}.{}".format(resultado[0], resultado[1], resultado[2], resultado[3]))


# Exercício 14 — Analisar um caminho de arquivo
caminho = input("Digite o caminho: ")

if caminho.endswith("/"):
    print("NULO")
else:
    primeira = caminho.find("/")
    ultima = caminho.rfind("/")
    arquivo = caminho[ultima + 1:]  # trecho após o último /

    print(primeira)
    print(ultima)

    if arquivo.endswith((".exe", ".bin", ".sh")):
        print("Executavel")
    else:
        print("Arquivo comum")


# Exercício 15 — Limpar um fragmento de transcrição
texto = input("Digite o fragmento de transcrição: ")


texto = texto.strip()
texto = texto.strip(" .,;:!?")
texto = texto.strip(" ^~")

if texto.startswith("[") or texto.endswith("]"):
    texto = texto.strip(" []")

print(f"Após a formatação ese eo seu texto: {texto}")


# Exercício 16 — Decifrar uma mensagem (a chave é o número de pontos no final)
mensagem = input("Digite a sua mensagem: ")

chave = len(mensagem) - len(mensagem.rstrip("."))
mensagem = mensagem.rstrip(".")
palavras = mensagem.split()

resultado = []
for palavra in palavras:
    if len(palavra) > 3:
        nova_palavra = ""
        for letra in palavra:
            nova_letra = chr(ord(letra) - chave)
            nova_palavra += nova_letra
        resultado.append(nova_palavra)
    else:
        resultado.append(palavra)


print(f"Transcrição: {' '.join(resultado)}")
