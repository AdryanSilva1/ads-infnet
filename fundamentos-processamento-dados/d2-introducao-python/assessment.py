# =============================================================
# Assessment — Introdução à Programação com Python
# Instituto Infnet — Bloco 01
# Autor: Adryan Da Silva Santos
#
# Observação:
# Arquivo organizado para portfólio acadêmico no GitHub.
# Cada exercício foi separado em uma função para evitar a execução
# automática de todos os inputs ao mesmo tempo.
# =============================================================


# -------------------------------------------------------------
# Exercício 1 – Custo de Produção
# -------------------------------------------------------------
def exercicio_01():
    valor_componente_a = float(input('Digite o custo unitário do componente_a: R$'))
    quantidade_componente_a = int(input('Digite a quantidade do componente_a: '))
    valor_componente_b = float(input('Digite o custo unitário do componente_b: R$'))
    quantidade_componente_b = int(input('Digite a quantidade do componente_b: '))
    custo_fixo_total = float(input('Digite o custo fixo total para todo o lote de produção: R$'))
    quantidade_total = int(input('Digite a quantidade total de produtos fabricados neste lote: '))

    custo_total_lote = (valor_componente_a * quantidade_componente_a * quantidade_total) + (valor_componente_b * quantidade_componente_b * quantidade_total) + custo_fixo_total
    custo_por_unidade = custo_total_lote / quantidade_total

    print(f"Custo total do lote de produção {custo_total_lote:.2f}")
    print(f"Custo por unidade do produto final {custo_por_unidade:.2f}")


# -------------------------------------------------------------
# Exercício 2 – Registro Inicial de Paciente
# -------------------------------------------------------------
def exercicio_02():
    nome_completo = input('Digite o nome completo do paciente: ')
    idade = int(input('Digite a idade do paciente: '))
    temperatura = float(input('Digite a temperatura corporal do paciente: ºC '))

    print(f"Nome: {nome_completo} | Idade: {idade} | Temperatura: {temperatura:.1f}ºC")


# -------------------------------------------------------------
# Exercício 3 – Soma e Média de Valores
# -------------------------------------------------------------
def exercicio_03():
    valores = [10, 20, 30, 40, 50]

    soma = sum(valores)
    media = soma / len(valores)

    print(f'Soma: {soma}')
    print(f'média: {media}')


# -------------------------------------------------------------
# Exercício 4 – Fatorial
# -------------------------------------------------------------
def exercicio_04():
    def fatorial(num):
        if num != 0:
            resultado = 1
            for c in range(num, 1, -1):
                resultado = resultado * c
        else:
            resultado = 1

        print(f'Fatorial de {num} = {resultado}')

    num = int(input("Digite um numero para saber seu fatorial: "))
    fatorial(num)


# -------------------------------------------------------------
# Exercício 5 – Conversor de Minutos
# -------------------------------------------------------------
def exercicio_05():
    def conversor(minutos):
        horas = minutos // 60
        mins = minutos % 60
        print(f'{horas}h {mins}min')

    minutos = int(input('Digite a duração total de um percurso em minutos: '))
    conversor(minutos)


# -------------------------------------------------------------
# Exercício 6 – Contador de Pares e Ímpares
# -------------------------------------------------------------
def exercicio_06():
    pares = 0
    impares = 0

    while True:
        insercao = input("Digite os numeros, para sair escreva SAIR:")

        if insercao == 'SAIR':
            print("Programa encerrado...")
            break
        elif int(insercao) % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"Impares: {impares}")
    print(f"Pares: {pares}")


# -------------------------------------------------------------
# Exercício 7 – Lista de Resultados
# -------------------------------------------------------------
def exercicio_07():
    def conta(passos):
        resultados = []

        for c in range(1, passos + 1):
            num = 1 - 10 ** (-c)
            y = (num ** 2 - 1) / (num - 1)

            resultados.append(y)

        print(f'A lista de resultado foi: {resultados}')

    passos = int(input('Digite a quamtidade de passos: '))
    conta(passos)


# -------------------------------------------------------------
# Exercício 8 – Velocidade Quadro a Quadro
# -------------------------------------------------------------
def exercicio_08():
    frame = [0.0, 0.45, 0.89, 1.32, 1.74, 2.15, 2.55, 2.94, 3.32, 3.69]
    quadro_a_quadro = []

    for c in range(1, len(frame)):
        posicao_anterior = frame[c - 1]
        posicao_atual = frame[c]

        velocidade = (posicao_atual - posicao_anterior) / 0.01

        quadro_a_quadro.append(velocidade)
        print(f"Frame {c}: {velocidade} m/s")

        if velocidade < 40:
            print('A bola está perdendo muita força!')
            break

    print(quadro_a_quadro)


# -------------------------------------------------------------
# Exercício 9 – Área Aproximada e Tinta Necessária
# -------------------------------------------------------------
def exercicio_09():
    import math

    area_total = 0

    def altura_parede(x):
        return math.sin(x) + 2

    n = int(input("Digite o numero de fatias: "))

    # largura da fatia
    delta_x = 10 / n

    for i in range(n):
        x = i * delta_x

        # area da fatia
        area_fatia = altura_parede(x) * delta_x

        # area total
        area_total += area_fatia

    # tinta necessaria
    tinta = area_total / 5

    # quantidade de latas
    latas = math.ceil(tinta / 3.6)

    print(f"A área total aproximada da parede: {area_total:.2f}m²")
    print(f"A quantidade total de tinta necessária: {tinta:.2f}L")
    print(f"O número mínimo de latas de 3,6L a serem compradas: {latas}")


# -------------------------------------------------------------
# Exercício 10 – Aplicação de Regras de Investimento
# -------------------------------------------------------------
def exercicio_10():
    def aplicacao_regras(capital_inicial, taxa_juros, duracao_investimento):
        # Regra de Penalidade
        if duracao_investimento < 3:
            valor_final = capital_inicial - (capital_inicial * 0.02)

        # Regra de Bônus
        elif duracao_investimento >= 18:
            bonus = capital_inicial + (capital_inicial * 0.005)
            valor_final = bonus * (1 + taxa_juros) ** duracao_investimento

        else:
            valor_final = capital_inicial * (1 + taxa_juros) ** duracao_investimento

        valor_final = int(valor_final * 100) / 100

        return valor_final

    capital_inicial = float(input('Digite o capital inicial: R$'))
    taxa_juros = float(input('Digite a taxa de juros mensal: '))
    duracao_investimento = int(input('Digite a quantidade de meses que o dinheiro ficara investido: '))

    valor_final = aplicacao_regras(capital_inicial, taxa_juros, duracao_investimento)

    print(f'''Com o investimento de: {capital_inicial}
Aplicando a taxa de: {taxa_juros}
Deixando {duracao_investimento} meses investido
Você tem o retorno de {valor_final:.2f}
''')


# -------------------------------------------------------------
# Exercício 11 – Duplicação entre Listas
# -------------------------------------------------------------
def exercicio_11():
    lista_a = []
    lista_b = []

    def duplicacao(a, b):
        duplicados = []

        for elemento in a:
            if elemento in b:
                duplicados.append(elemento)

        return duplicados

    while True:
        print("=" * 10, "Comece a digitara a lista A", "=" * 10)

        while True:
            item = input("Digite a lista A, para parar digite SAIR:")

            if item == 'SAIR':
                print("=" * 10, "Comece a digitara a lista B", "=" * 10)
                break

            else:
                lista_a.append(item)

        while True:
            item = input("Digite a lista B, para parar digite SAIR:")

            if item == 'SAIR':
                break

            else:
                lista_b.append(item)

        break

    resultado = duplicacao(lista_a, lista_b)

    print("=" * 10, "Resultado", "=" * 10)
    print(resultado)


# -------------------------------------------------------------
# Exercício 12 – Estimativa de Pi
# -------------------------------------------------------------
def exercicio_12():
    import random

    valores = [10, 100, 1000, 10000, 100000]

    def estimar_pi(total_pontos):
        dentro = 0

        for c in range(total_pontos):
            x = random.random()
            y = random.random()

            if x ** 2 + y ** 2 <= 1:
                dentro += 1

        pi = 4 * (dentro / total_pontos)
        return pi

    for total_pontos in valores:
        pi = estimar_pi(total_pontos)
        print(f'A estimativa para o pi de {total_pontos} é: {pi}')


# -------------------------------------------------------------
# Exercício 13 – Comparação de Gabarito
# -------------------------------------------------------------
def exercicio_13():
    gabarito = ['A', 'B', 'C', 'D', 'E']
    aluno1 = ['A', 'B', 'D', 'D', 'E']
    aluno2 = ['A', 'C', 'C', 'D', 'F']

    acertos_al1 = 0
    acertos_al2 = 0

    for c in range(len(gabarito)):
        if gabarito[c] == aluno1[c]:
            acertos_al1 += 1

        if gabarito[c] == aluno2[c]:
            acertos_al2 += 1

    print(f'acertos do aluno1: {acertos_al1}')
    print(f'acertos do aluno2: {acertos_al2}')

    print('=' * 10, " QUEM É O GANHADOR? ", '=' * 10)

    if acertos_al1 > acertos_al2:
        print('Aluno 1 venceu')

    elif acertos_al1 < acertos_al2:
        print('Aluno 2 venceu')

    else:
        print('Empate')


# -------------------------------------------------------------
# Exercício 14 – Validação de CPF
# -------------------------------------------------------------
def exercicio_14():
    def validar_cpf(cpf):
        if len(cpf) != 11:
            return "CPF Inválido"

        if not cpf.isdigit():
            return "CPF Inválido"

        if len(set(cpf)) == 1:
            return "CPF Inválido"

        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)

        resto = soma % 11
        digito1 = 11 - resto
        if digito1 >= 10:
            digito1 = 0

        if digito1 != int(cpf[9]):
            return "CPF Inválido"

        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)

        resto = soma % 11
        digito2 = 11 - resto
        if digito2 >= 10:
            digito2 = 0

        if digito2 != int(cpf[10]):
            return "CPF Inválido"

        return "CPF Válido"

    cpf = input("Digite seu CPF: ")

    resultado = validar_cpf(cpf)

    if resultado == "CPF Válido":
        print("Tudo certo! Seu CPF é válido.")
    else:
        print(" Seu CPF inválido. Verifique os dados e tente novamente.")


# -------------------------------------------------------------
# Exercício 15 – Meta de Arrecadação
# -------------------------------------------------------------
def exercicio_15():
    meta = int(input("digite a meta de arrecadações: "))
    doados = 0

    while doados < meta:
        doacao = float(input("Digite a sua doação: "))
        doados += doacao

    if doados == meta:
        mensagem = "Meta atingida"
    else:
        mensagem = f"Meta superada em {doados - meta:.2f}"

    print(f"{doados:.2f} - {mensagem}")


# -------------------------------------------------------------
# Exercício 16 – Movimento em Grid
# -------------------------------------------------------------
def exercicio_16():
    def mover_personagem(x, y, comando):
        comando = comando.lower()

        if comando == 'w':
            if y > 0:
                y -= 1
            else:
                print("Colisão com a fronteira!")

        elif comando == 's':
            if y < 19:
                y += 1
            else:
                print("Colisão com a fronteira!")

        elif comando == 'a':
            if x > 0:
                x -= 1
            else:
                print("Colisão com a fronteira!")

        elif comando == 'd':
            if x < 19:
                x += 1
            else:
                print("Colisão com a fronteira!")

        return x, y

    def mostrar_grid(x, y, bx, by):
        for linha in range(20):
            for coluna in range(20):
                if coluna == x and linha == y:
                    print("P", end="")
                elif coluna == bx and linha == by:
                    print("B", end="")
                else:
                    print(".", end="")
            print()

    x = 3
    y = 2

    bandeira_x = 15
    bandeira_y = 18

    mostrar_grid(x, y, bandeira_x, bandeira_y)

    while True:
        comando = input("Digite um comando (w, a, s, d ou sair): ")

        if comando.lower() == "sair":
            break

        x, y = mover_personagem(x, y, comando)

        mostrar_grid(x, y, bandeira_x, bandeira_y)

        if x == bandeira_x and y == bandeira_y:
            print("Objetivo alcançado! Missão cumprida.")
            break


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
    print("Assessment — Introdução à Programação com Python")
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
