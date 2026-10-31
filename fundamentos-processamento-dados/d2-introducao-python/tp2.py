# =============================================================
# Teste de Performance 2 — Introdução à Programação com Python
# Instituto Infnet — Bloco 01
# Autor: Adryan Da Silva Santos
# Aproveitamento: 75%
# Observação:
# Arquivo organizado para portfólio acadêmico no GitHub.
# Cada exercício foi separado em uma função para evitar a execução
# automática de todos os inputs ao mesmo tempo.
# =============================================================


# -------------------------------------------------------------
# Exercício 1 – Cabeçalho Multilinha
# -------------------------------------------------------------
def exercicio_01():
    cabecalho = '''Nome do módulo: Módulo de Vendas Diretas
Data de criação: 15/03/2024
Descrição: Responsável pelo registro e acompanhamento das vendas da equipe externa..'''
    print(cabecalho)


# -------------------------------------------------------------
# Exercício 2 – Geração de SKU
# -------------------------------------------------------------
def exercicio_02():
    prefixo = 'ELT'
    numero_serie = '12345'
    sku = prefixo + numero_serie
    print(f"Seu código SKU é: {sku}")


# -------------------------------------------------------------
# Exercício 3 – Linha de Separação para Relatórios
# -------------------------------------------------------------
def exercicio_03():
    caractere = '-'
    repeticoes = 30

    print(caractere * repeticoes)


# -------------------------------------------------------------
# Exercício 4 – Mensagem Recebida e Capitalização Invertida
# -------------------------------------------------------------
def exercicio_04():
    mensagem = input("Digite uma mensagem: ")
    print("Sua mensagem '{}' foi recebida com sucesso".format(mensagem))
    print(mensagem.swapcase())


# -------------------------------------------------------------
# Exercício 5 – Formatação de Nomes para Crachás
# -------------------------------------------------------------
def exercicio_05():
    nome_completo = input("Digite o nome completo: ").upper()
    nome_cracha = input("Digite o nome para o crachá: ").capitalize()

    seguranca = nome_cracha + "---" + nome_completo

    print(nome_completo)
    print(nome_cracha)
    print(seguranca)


# -------------------------------------------------------------
# Exercício 6 – Verificador de Conformidade de Senha
# -------------------------------------------------------------
def exercicio_06():
    senha = input("Digite sua senha: ")

    senha_arroba = '@' in senha
    senha_exclamacao = '!' in senha
    senha_hastag = '#' in senha
    senha_maiuscula = senha.isupper()
    senha_minuscula = senha.islower()

    print(f"Senha com @: {senha_arroba}")
    print(f"Senha com !: {senha_exclamacao}")
    print(f"Senha com #: {senha_hastag}")
    print(f"Senha em maiúscula: {senha_maiuscula}")
    print(f"Senha em minúscula: {senha_minuscula}")


# -------------------------------------------------------------
# Exercício 7 – Verificador de Limite de SMS
# -------------------------------------------------------------
def exercicio_07():
    mensagem_candidata = 'Desconto exclusivo para você! Válido por tempo limitado.'
    prefixo_padrao = 'Voz Digital: '
    sufixo_padrao = ' Acesse nosso site para detalhes.'

    mensagem = prefixo_padrao + mensagem_candidata + sufixo_padrao
    tamanho_total = len(mensagem)
    diferenca_limite = 160 - tamanho_total

    print(f"O tamanho total da mensagem é de {tamanho_total} caracteres.")
    print(f"A diferença em relação ao limite de 160 caracteres é de {diferenca_limite} caracteres.")


# -------------------------------------------------------------
# Exercício 8 – Cartão ASCII de Boas-Vindas
# -------------------------------------------------------------
def exercicio_08():
    cartao = "="*35 + "\n" + "=" + " "*33 + "=" + "\n"  + "=" + " "*33 + "=" + "\n"+ "="*35
    print(cartao)


# -------------------------------------------------------------
# Exercício 9 – Construção de URLs de API
# -------------------------------------------------------------
def exercicio_09():
    dominio_base = 'api.linkmanager.com'
    caminho = 'clientes'
    identificador = '123'
    acao = 'detalhes'
    print(f"A URL gerada foi: {dominio_base}/{caminho}/{identificador}/{acao}")


# -------------------------------------------------------------
# Exercício 10 – Contagem de Hashtags em Postagens
# -------------------------------------------------------------
def exercicio_10():
    texto = 'Participe do nosso #PythonChallenge e conquiste prêmios! #pythonchallenge agora mesmo!'

    quantidade_exata = texto.count("#PythonChallenge")
    quantidade_minuscula = texto.count("#pythonchallenge")

    print(f"#PythonChallenge apareceu {quantidade_exata} vez(es) no texto")
    print(f"#pythonchallenge apareceu {quantidade_minuscula} vez(es) no texto")


# -------------------------------------------------------------
# Exercício 11 – Gestão de Estoque após Retirada
# -------------------------------------------------------------
def exercicio_11():
    quantidade_total = int(input("Qual é a quantidade total do produto? "))
    reducao = int(input("Qual é a quantidade que será retirada do produto? "))
    estoque = quantidade_total - reducao
    print(f"Após a retirada de {reducao} itens, o saldo atual é de {estoque} unidades.")


# -------------------------------------------------------------
# Exercício 12 – Cálculo de Parcelamento com Juros
# -------------------------------------------------------------
def exercicio_12():
    preco = float(input("Informe o preço à vista do produto: "))
    taxa_juros = float(input("Informe a taxa de juros mensal (ex: 0.02 para 2%): "))
    meses = int(input("Informe o número de parcelas: "))
    taxa_admin = float(input("Informe a taxa administrativa (ex: 0.05 para 5%): "))

    valor_com_juros = preco * (1 + taxa_juros * meses) * (1 + taxa_admin)

    print(f"o valor final de seu produto: {valor_com_juros:.2f}")
    print(f"O valor de cada parcela: {valor_com_juros/meses:.2f}")


# -------------------------------------------------------------
# Exercício 13 – Pontuação Final em Arcana Quest ⚠️ INCOMPLETO
# -------------------------------------------------------------
def exercicio_13():
    fase_exploracao = str(input("Digite a pontução da sua exploração: "))
    fase_combate = str(input("Digite a pontução do seu combate: "))
    fase_estrategia = str(input("Digite a pontução da sua estrategia: "))

    ponto_total = int(fase_exploracao) + int(fase_combate) + int(fase_estrategia)

    print(f"Pontuação Final em Arcana Quest: {ponto_total} pontos.")


# -------------------------------------------------------------
# Exercício 14 – Conversão de Temperatura e IET
# -------------------------------------------------------------
def exercicio_14():
    temperatura_celsius = float(input("digite a temperatura em graus: "))

    fahrenheit = (temperatura_celsius * 9 / 5) + 32
    iet = (temperatura_celsius / 4.0) - (temperatura_celsius * 0.08) + 1.5

    print(f"{fahrenheit:.2f}; {iet:.2f}")


# -------------------------------------------------------------
# Exercício 15 – Porcentagem de Vogais em Mensagem
# -------------------------------------------------------------
def exercicio_15():
    # Recebe a mensagem e converte para minúsculo para facilitar comparação
    mensagem = input("Digite uma mensagem: ").lower()

    # Contador de vogais
    quantidade = 0

    # Percorre cada letra e verifica se é vogal
    for letra in mensagem:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            quantidade = quantidade + 1

    # Calcula a porcentagem
    porcentagem = (quantidade / len(mensagem)) * 100

    print(f"{porcentagem:.2f}%")


# -------------------------------------------------------------
# Exercício 16 – Log de Transação Financeira
# -------------------------------------------------------------
def exercicio_16():
    id_transacao = input("informe o id da sua transacao: ")
    data = input("informe a data (AAAA-MM-DD): ")
    hora = input("Informe a hora (HH:MM:SS): ")
    tipo = input("informe o tipo DEB (débito) ou CRED (crédito): ")
    conta_origem = input("Informe o numero da conta de origem: ")
    conta_destino = input("Informe o numero da conta de destino: ")
    valor = input("informe o valor da transferencia: ")

    log = f"[LOG: {id_transacao}] - DATA: {data} {hora} | TIPO: {tipo} {{ORIGEM: {conta_origem} -> DESTINO: {conta_destino}}} VALOR: R${valor};"
    print(log)


# -------------------------------------------------------------
# Menu principal
# -------------------------------------------------------------
def menu():
    exercicios = {
        "1": exercicio_01,
        "2": exercicio_02,
        "3": exercicio_03,
        "4": exercicio_04,
        "5": exercicio_05,
        "6": exercicio_06,
        "7": exercicio_07,
        "8": exercicio_08,
        "9": exercicio_09,
        "10": exercicio_10,
        "11": exercicio_11,
        "12": exercicio_12,
        "13": exercicio_13,
        "14": exercicio_14,
        "15": exercicio_15,
        "16": exercicio_16,
    }

    print("=" * 60)
    print("TP2 — Introdução à Programação com Python")
    print("Escolha um exercício de 1 a 16 para executar.")
    print("=" * 60)

    escolha = input("Número do exercício: ").strip()

    if escolha in exercicios:
        print("-" * 60)
        exercicios[escolha]()
    else:
        print("Exercício inválido.")


if __name__ == "__main__":
    menu()
