# =============================================================
# Teste de Performance 3 — Introdução à Programação com Python
# Instituto Infnet — Bloco 01
# Autor: Adryan Da Silva Santos
# Aproveitamento: 100%
# Observação:
# Arquivo organizado para portfólio acadêmico no GitHub.
# Cada exercício foi separado em uma função para evitar a execução
# automática de todos os inputs ao mesmo tempo.
# =============================================================


# -------------------------------------------------------------
# Exercício 1 — Verificação de idade para compra
# -------------------------------------------------------------
def exercicio_01():
    idade_cliente = int(input("Digite a sua idade: "))

    if idade_cliente >= 18:
        print("Compra autorizada.")
    else:
        print("Compra negada.")


# -------------------------------------------------------------
# Exercício 2 — Verificação de aprovação acadêmica
# -------------------------------------------------------------
def exercicio_02():
    while True:
        nota_final = int(input("Digite a nota final do estudante (0 a 100): "))
        if 0 <= nota_final <= 100:
            break
        print("Nota final inválida. Tente novamente com um valor válido.")

    while True:
        nota_minima = int(input("Digite a nota mínima (0 a 100): "))
        if 0 <= nota_minima <= 100:
            break
        print("Nota mínima inválida. Tente novamente com um valor válido.")

    if nota_final >= nota_minima:
        print("APROVADO")
    else:
        print("REPROVADO")


# -------------------------------------------------------------
# Exercício 3 — Análise de temperatura corporal
# -------------------------------------------------------------
def exercicio_03():
    temperatura_paciente = float(input("Digite a temperatura do paciente: "))

    if 37.5 <= temperatura_paciente < 38.0:
        print("Estado febril")
    elif temperatura_paciente >= 38.0:
        print("Há febre")


# -------------------------------------------------------------
# Exercício 4 — Controle de peso de pacotes
# -------------------------------------------------------------
def exercicio_04():
    peso_pacote = float(input("Digite o peso em quilogramas (kg): "))

    if peso_pacote > 10.0:
        print("Excesso de peso")
    elif 9.5 <= peso_pacote <= 10.0:
        print("Peso próximo ao limite. Verificar embalagem.")
    else:
        print("Permitido")


# -------------------------------------------------------------
# Exercício 5 — Classificação de despesas pessoais
# -------------------------------------------------------------
def exercicio_05():
    descricao = input("Digite a descrição: ").lower()
    valor_despesa = input("Digite o valor da despesa: ")

    termos_essenciais = [
        "aluguel", "moradia", "supermercado",
        "alimentacao", "agua", "luz", "internet"
    ]

    termos_investimento = ["acoes", "fundos", "previdencia", "bolsa"]

    if any(termo in descricao for termo in termos_essenciais):
        categoria = "Essencial"
    elif any(termo in descricao for termo in termos_investimento):
        categoria = "Investimento"
    else:
        categoria = "Lazer e Outros"

    print(f"{categoria} - {valor_despesa}")


# -------------------------------------------------------------
# Exercício 6 — Verificação de atributos de personagem
# -------------------------------------------------------------
def exercicio_06():
    while True:
        forca = int(input("Digite a força do seu personagem: "))
        if forca > 0:
            break
        print("Força inválida. Tente novamente.")

    while True:
        agilidade = int(input("Digite a agilidade do seu personagem: "))
        if agilidade > 0:
            break
        print("Agilidade inválida. Tente novamente.")

    if forca > 75 and agilidade > 80:
        print("QUALIFICADO")
    else:
        print("NAO QUALIFICADO")


# -------------------------------------------------------------
# Exercício 7 — Cálculo de desconto progressivo
# -------------------------------------------------------------
def exercicio_07():
    while True:
        preco = float(input("Digite o valor total da compra: R$ "))
        if preco > 0:
            break
        print("Preço inválido. Tente novamente.")

    cartao = input("O pagamento é realizado com o cartão TecnoMais (S/N)? ").strip().lower()

    if preco <= 100.00:
        desconto = 0
    elif preco <= 500.00:
        desconto = 5
    elif preco <= 1000.00:
        desconto = 10
    else:
        desconto = 15

    if cartao == "s" and desconto > 0:
        desconto += 2

    valor_final = preco * (1 - desconto / 100)

    print(f"{valor_final:.2f}")


# -------------------------------------------------------------
# Exercício 8 — Triagem de candidato para entrevista
# -------------------------------------------------------------
def exercicio_08():
    experiencia = int(input("Anos de experiência: "))
    escolaridade = input("Escolaridade: ").lower()
    nivel_python = input("Nível em Python: ").lower()

    possui_formacao_avancada = escolaridade in ["pós-graduação", "pos-graduacao", "mestrado"]
    possui_python_avancado = nivel_python == "avançado" or nivel_python == "avancado"
    possui_infnet = "infnet" in escolaridade or "infnet" in nivel_python

    if experiencia >= 8 or (possui_formacao_avancada and possui_python_avancado) or possui_infnet:
        print("Candidato Elegível")
    else:
        print("Candidato Não Elegível")


# -------------------------------------------------------------
# Exercício 9 — Caverna dos Caminhos Incertos
# -------------------------------------------------------------
def exercicio_09():
    caminho = input("Caminho (Esquerda/Direita): ").capitalize()

    if caminho == "Esquerda":
        coragem = int(input("Nível de coragem (0 a 100): "))

        if coragem >= 80:
            print("Tesouro Encontrado")
        else:
            vida = int(input("Nível de vida restante (0 a 100): "))

            if vida >= 30:
                print("Fuga Bem-Sucedida")
            else:
                print("Derrota na Caverna")

    elif caminho == "Direita":
        tocha = input("Possui tocha? (Sim/Nao): ").capitalize()

        if tocha == "Nao":
            print("Perdido na Escuridao")
        else:
            tempo = int(input("Tempo restante da tocha (minutos): "))

            if tempo > 10:
                print("Caminho Seguro")
            else:
                print("Avanco Arriscado")


# -------------------------------------------------------------
# Exercício 10 — Pontuação de jogador no BattleQuest
# -------------------------------------------------------------
def exercicio_10():
    inimigos = int(input("Inimigos derrotados: "))
    objetivos = int(input("Objetivos conquistados: "))
    mortes = int(input("Mortes sofridas: "))
    tempo = int(input("Tempo de partida (min): "))

    if inimigos < 10:
        pontos_inimigos = 10
    elif inimigos <= 29:
        pontos_inimigos = 30
    else:
        pontos_inimigos = 50

    if objetivos == 0:
        pontos_objetivos = 0
    elif objetivos <= 2:
        pontos_objetivos = 25
    else:
        pontos_objetivos = 60

    if mortes < 5:
        penalidade_mortes = 0
    elif mortes <= 10:
        penalidade_mortes = -10
    else:
        penalidade_mortes = -30

    if tempo < 5:
        pontos_tempo = 25
    elif tempo <= 14:
        pontos_tempo = 15
    else:
        pontos_tempo = 5

    pontuacao = pontos_inimigos + pontos_objetivos + penalidade_mortes + pontos_tempo

    print(f"Pontuação final: {pontuacao}")

    if pontuacao > 100:
        print("Parabéns, você é um Jogador Elite!")


# -------------------------------------------------------------
# Exercício 11 — Classificação de força de senha
# -------------------------------------------------------------
def exercicio_11():
    senha = input("Digite sua senha: ")
    criterios = 0

    if len(senha) >= 8:
        criterios += 1

    tem_especial = False
    for caractere in senha:
        if caractere in ["!", "@", "#"]:
            tem_especial = True

    if tem_especial:
        criterios += 1

    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True

    if tem_numero:
        criterios += 1

    if criterios >= 2:
        print("Segura")
    else:
        print("Fraca")


# -------------------------------------------------------------
# Exercício 12 — Classificação de alerta meteorológico
# -------------------------------------------------------------
def exercicio_12():
    vento = int(input("Velocidade do vento (km/h): "))
    temperatura = int(input("Temperatura (°C): "))
    umidade = int(input("Umidade (%): "))
    precipitacao = input("Precipitação (Chuva/Neve/Granizo/Nenhum): ").capitalize()

    if vento > 80 or (precipitacao == "Granizo" and vento > 60):
        print("ALERTA VERMELHO (Perigo Iminente)")

    elif (
        temperatura < -10
        or (precipitacao == "Neve" and vento > 40)
        or (precipitacao == "Neve" and temperatura < 0)
        or vento > 50
    ):
        print("ALERTA LARANJA (Cuidado)")

    elif (
        (precipitacao == "Chuva" and vento > 40 and umidade > 90)
        or vento > 20
        or umidade > 80
    ):
        print("ALERTA AMARELO (Atenção)")

    elif (
        (precipitacao == "Nenhum" and temperatura < 5 and vento > 30)
        or temperatura < 10
        or umidade > 75
        or precipitacao == "Chuva"
    ):
        print("ALERTA AZUL (Observação)")

    else:
        print("SEM ALERTA")


# -------------------------------------------------------------
# Exercício 13 — Calculadora básica
# -------------------------------------------------------------
def exercicio_13():
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    operacao = input("Operação (soma/subtracao/multiplicacao/divisao): ").lower()

    if operacao == "soma":
        print(num1 + num2)
    elif operacao == "subtracao":
        print(num1 - num2)
    elif operacao == "multiplicacao":
        print(num1 * num2)
    elif operacao == "divisao":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Erro: divisão por zero não permitida.")


# -------------------------------------------------------------
# Exercício 14 — Compatibilidade para doação de sangue
# -------------------------------------------------------------
def exercicio_14():
    tipo_receptor = input("Tipo sanguíneo do receptor (A/B/AB/O): ").upper()
    rh_receptor = input("Fator Rh do receptor (+/-): ")
    tipo_doador = input("Tipo sanguíneo do doador (A/B/AB/O): ").upper()
    rh_doador = input("Fator Rh do doador (+/-): ")

    if tipo_receptor == "A":
        tipo_compativel = tipo_doador in ["A", "O"]
    elif tipo_receptor == "B":
        tipo_compativel = tipo_doador in ["B", "O"]
    elif tipo_receptor == "AB":
        tipo_compativel = tipo_doador in ["A", "B", "AB", "O"]
    elif tipo_receptor == "O":
        tipo_compativel = tipo_doador == "O"
    else:
        tipo_compativel = False

    if rh_receptor == "+":
        rh_compativel = rh_doador in ["+", "-"]
    else:
        rh_compativel = rh_doador == "-"

    if tipo_compativel and rh_compativel:
        print("Doacao compativel")
    else:
        print("Doacao incompatível")


# -------------------------------------------------------------
# Exercício 15 — Jogo das Engrenagens Eternas
# -------------------------------------------------------------
def exercicio_15():
    a = int(input("Prova A: "))
    b = int(input("Prova B: "))
    c = int(input("Prova C: "))
    d = int(input("Prova D: "))

    regra1 = (15 < a < 45) and b <= 60
    regra2 = c == 1 or (c == 0 and a < 20 and b < 30 and d == 10)
    regra3 = d >= 5 or (d < 5 and (a == 10 or a == 40) and b == 0)

    if regra1 and regra2 and regra3:
        print("APROVADO")
    else:
        print("REPROVADO")


# -------------------------------------------------------------
# Exercício 16 — Triagem cadastral de cliente
# -------------------------------------------------------------
def exercicio_16():
    tipo = input("Tipo de cliente (PF/PJ): ").upper()

    if tipo == "PF":
        cpf = input("CPF (apenas números): ")
        idade = int(input("Idade: "))

        if len(cpf) == 11 and idade >= 18:
            print("Cadastro Aprovado")
        else:
            doc = input("Possui documentação complementar? (S/N): ").upper()

            if doc == "S" and idade >= 18:
                print("Cadastro em Revisao")
            else:
                print("Cadastro Recusado")

    elif tipo == "PJ":
        cnpj = input("CNPJ (apenas números): ")

        if len(cnpj) == 14:
            print("Cadastro Aprovado")
        else:
            registro = input("Possui registro provisório? (S/N): ").upper()

            if registro == "S":
                print("Cadastro em Revisao")
            else:
                print("Cadastro Recusado")

    else:
        print("Tipo de cliente inválido!")


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
    print("TP3 — Introdução à Programação com Python")
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
