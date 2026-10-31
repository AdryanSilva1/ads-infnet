# =============================================================
# TP1 — Introdução à Programação com Python
# Instituto Infnet — Bloco 01
# Aproveitamento: 100%
# Autor: Adryan Da Silva Santos
# Observação:

# =============================================================


def exercicio_01():
    """Exercício 1 — Importância da Programação e Comentários"""

    # A automação com Python ajuda a empresa a ganhar tempo, reduzir erros manuais
    # e padronizar processos do dia a dia, com scripts bem documentados, qualquer
    # desenvolvedor consegue entender rapidamente o objetivo do código e dar
    # continuidade ao trabalho com mais eficiência.


def exercicio_02():
    """Exercício 2 — Processo de Escrita e Hello World"""

    print("Olá Mundo! Bem-vindo ao Cinema Digital")


def exercicio_03():
    """Exercício 3 — Abordagem Programática e Atribuição"""

    disciplina = "Python"
    turma = 101

    print(f"Diciplina: {disciplina}")
    print(f"Turma: {turma}")


def exercicio_04():
    """Exercício 4 — Fluxo IPO: Entrada, Processamento e Saída"""

    # Entrada
    peso_unidade = 80
    quantidade = 10

    # Processamento
    peso_total = peso_unidade * quantidade

    # Saída
    print(f"Peso total: {peso_total} Kg")


def exercicio_05():
    """Exercício 5 — Atribuição de Variáveis de Inventário"""

    quantidade_macas = 150
    preco_maca = 5.99

    print(f"Quantidade de macas: {quantidade_macas}")
    print(f"Preço de macas: R${preco_maca:.2f}")


def exercicio_06():
    """Exercício 6 — Tipos Básicos: Int e Float no Financeiro"""

    contratos = 12
    faturamento = 2500.50

    print(f"Tipo da variável contratos: {type(contratos).__name__}")
    print(f"Tipo da variável faturamento: {type(faturamento).__name__}")


def exercicio_07():
    """Exercício 7 — Tipos Básicos: Booleanos em Segurança"""

    sensor_ativo = True
    print(f"Estado do sensor: {sensor_ativo}")

    sensor_ativo = False
    print(f"Estado do sensor: {sensor_ativo}")


def exercicio_08():
    """Exercício 8 — Operações Aritméticas: Soma de Receita"""

    venda_smartphones = 5400.00
    venda_acessorios = 1250.50

    receita_total = venda_smartphones + venda_acessorios

    print(f"Receita total: R${receita_total:.2f}")


def exercicio_09():
    """Exercício 9 — Operações de Subtração de Saldo"""

    saldo_atual = 10000
    valor_fatura = 3500

    saldo_final = saldo_atual - valor_fatura

    print(f"Saldo final após o pagamento: R${saldo_final:.2f}")


def exercicio_10():
    """Exercício 10 — Multiplicação e Divisão de Preços"""

    preco_fardo = 24.0
    unidades = 6

    preco_unitario = preco_fardo / unidades

    print(f"Preço por unidade: R${preco_unitario:.2f}")


def exercicio_11():
    """Exercício 11 — Otimização de Carga e Estabilidade de Frete"""

    capacidade_maxima = 550
    peso_saca = 65
    carga_atual = 0
    quantidade_sacas = 0

    while carga_atual + peso_saca <= capacidade_maxima:
        carga_atual += peso_saca
        quantidade_sacas += 1

    porcentagem_ocupacao = (carga_atual / capacidade_maxima) * 100

    print(f"Sacas carregadas: {quantidade_sacas}")
    print(f"Carga total no caminhão: {carga_atual} kg")
    print(f"Ocupação do caminhão: {porcentagem_ocupacao:.2f}%")


def exercicio_12():
    """Exercício 12 — Sincronização de Turnos e Manutenção Preventiva"""

    dias_decorridos = 125
    periodicidade = 8

    dia_atual_do_ciclo = dias_decorridos % periodicidade
    dias_faltando = periodicidade - dia_atual_do_ciclo
    dias_totais_parada = dias_decorridos + dias_faltando

    print(f"Dia atual dentro do ciclo: {dia_atual_do_ciclo}")
    print(f"Dias restantes para o fim do ciclo: {dias_faltando}")
    print(f"Parada técnica prevista para o dia: {dias_totais_parada}")


def exercicio_13():
    """Exercício 13 — Engenharia Reversa de Tributação e Logística"""

    custo_base = 2500
    aliquota = 0.05
    suporte = 150

    print(f"Valor final: R${custo_base + (custo_base * aliquota) + suporte:.2f}")


def exercicio_14():
    """Exercício 14 — Auditoria de Desempenho e Eficiência de Ativos"""

    minutos = 345
    horas = minutos / 60

    print(f"O valor convertido: {horas:.2f} h")


def exercicio_15():
    """Exercício 15 — Telemetria Aeroespacial e Autonomia de Voo"""

    segundos_voo1 = 3.77 * 3600
    segundos_voo2 = 214 * 60
    segundos_totais = segundos_voo1 + segundos_voo2
    energia = segundos_totais * 2.7
    energia_final = energia * 1.15

    print(f"Tempo total em segundos: {segundos_totais:.2f}s")
    print(f"Energia necessária com segurança: {energia_final:.2f} J")


def exercicio_16():
    """Exercício 16 — Decomposição de Jornada para Fechamento de Folha"""

    minutos_totais = 1527

    horas = minutos_totais // 60
    minutos_excedentes = minutos_totais % 60

    valor_horas = horas * 60
    valor_minutos = minutos_excedentes * 1.20
    valor_total = valor_horas + valor_minutos

    print(f"Horas trabalhadas: {horas}h")
    print(f"Minutos excedentes: {minutos_excedentes}min")
    print(f"Valor pelas horas: R${valor_horas:.2f}")
    print(f"Valor pelos minutos: R${valor_minutos:.2f}")
    print(f"Valor total a receber: R${valor_total:.2f}")


EXERCICIOS = {
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


def exibir_menu():
    print("\n" + "=" * 60)
    print("TP1 — Introdução à Programação com Python")
    print("=" * 60)
    print("Digite o número do exercício que deseja executar.")
    print("Digite 0 para sair.")
    print("-" * 60)

    for numero in range(1, 17):
        print(f"{numero:02d} — Exercício {numero}")

    print("=" * 60)


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Execução finalizada.")
            break

        exercicio = EXERCICIOS.get(opcao)

        if exercicio is None:
            print("Opção inválida. Tente novamente.")
            continue

        print("\n" + "-" * 60)
        print(f"Executando exercício {opcao}")
        print("-" * 60)
        exercicio()


if __name__ == "__main__":
    main()
