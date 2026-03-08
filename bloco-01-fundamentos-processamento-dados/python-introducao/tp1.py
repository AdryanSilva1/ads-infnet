# =============================================================
# Teste de Performance 1 — Introdução à Programação com Python
# Instituto Infnet — Bloco 01
# Adryan Da Silva Santos
# =============================================================


# ---------------------------------------------------------------
# Exercício 1 – Importância da Programação e Comentários
# Uma consultoria de tecnologia está integrando novos desenvolvedores
# e deseja padronizar a documentação inicial de seus scripts. O setor
# de treinamento precisa que todo código comece com uma explicação clara
# sobre por que a automação via Python é vital para a eficiência da empresa.
#
# Tarefa: Utilize o caractere # para escrever um comentário explicativo
# sobre a importância da programação.
# ---------------------------------------------------------------

# A automação com Python ajuda a empresa a ganhar tempo, reduzir erros manuais
# e padronizar processos do dia a dia, com scripts bem documentados, qualquer
# desenvolvedor consegue entender rapidamente o objetivo do código e dar
# continuidade ao trabalho com mais eficiência.


# ---------------------------------------------------------------
# Exercício 2 – Processo de Escrita e Hello World
# O departamento de marketing de uma rede de cinemas quer testar a interface
# de seus novos totens de autoatendimento. O programa deve exibir a saudação
# oficial solicitada pela gerência na tela do terminal.
#
# Tarefa: Utilize a função print() para exibir a mensagem:
# "Olá Mundo! Bem-vindo ao Cinema Digital"
# ---------------------------------------------------------------

print("Olá Mundo! Bem-vindo ao Cinema Digital")


# ---------------------------------------------------------------
# Exercício 3 – Abordagem Programática e Atribuição
# O setor de RH de uma escola de cursos livres deseja preparar o sistema
# para o registro de novos alunos. O cenário envolve o armazenamento do
# nome de uma disciplina e o código da turma.
#
# Tarefa: Declare disciplina = "Python" e turma = 101.
# Utilize dois print() separados para exibir cada variável.
# ---------------------------------------------------------------

disciplina = "Python"
turma = 101

print(f"Diciplina: {disciplina}")
print(f"Turma: {turma}")


# ---------------------------------------------------------------
# Exercício 4 – Fluxo IPO: Entrada, Processamento e Saída
# Uma equipe de logística precisa de um utilitário para registrar dados
# de estoque seguindo uma estrutura organizada de entrada, processamento
# e saída (IPO).
#
# Tarefa: Crie peso_unidade = 80 e quantidade = 10.
# Calcule peso_total e exiba o resultado.
# ---------------------------------------------------------------

# Entrada
peso_unidade = 80
quantidade = 10

# Processamento
peso_total = peso_unidade * quantidade

# Saída
print(f"Peso total: {peso_total} Kg")


# ---------------------------------------------------------------
# Exercício 5 – Atribuição de Variáveis de Inventário
# O gerente de um pequeno hortifruti deseja digitalizar o controle
# de seus itens mais vendidos.
#
# Tarefa: Atribua quantidade_macas = 150 e preco_maca = 5.99.
# Exiba primeiro a quantidade e depois o preço em linhas separadas.
# ---------------------------------------------------------------

quantidade_macas = 150
preco_maca = 5.99

print(f"Quantidade de macas: {quantidade_macas}")
print(f"Preço de macas: R${preco_maca:.2f}")


# ---------------------------------------------------------------
# Exercício 6 – Tipos Básicos: Int e Float no Financeiro
# Um analista financeiro está criando um controle de contratos para
# uma microempresa. O programa deve confirmar os tipos de dados processados.
#
# Tarefa: Crie contratos = 12 e faturamento = 2500.50.
# Exiba o tipo de cada variável utilizando type().
# ---------------------------------------------------------------

contratos = 12
faturamento = 2500.50

print(f"Tipo da variável contratos: {type(contratos).__name__}")
print(f"Tipo da variável faturamento: {type(faturamento).__name__}")


# ---------------------------------------------------------------
# Exercício 7 – Tipos Básicos: Booleanos em Segurança
# Uma empresa de segurança patrimonial precisa de um verificador para
# o estado dos sensores de um armazém.
#
# Tarefa: Crie sensor_ativo = True, exiba o valor, altere para False
# e imprima novamente.
# ---------------------------------------------------------------

sensor_ativo = True
print(f"Estado do sensor: {sensor_ativo}")

sensor_ativo = False
print(f"Estado do sensor: {sensor_ativo}")


# ---------------------------------------------------------------
# Exercício 8 – Operações Aritméticas: Soma de Receita
# O setor de vendas de uma loja de eletrônicos precisa calcular
# a receita bruta do período da manhã.
#
# Tarefa: Defina venda_smartphones = 5400.00 e venda_acessorios = 1250.50.
# Crie receita_total com a soma e exiba o resultado.
# ---------------------------------------------------------------

venda_smartphones = 5400.00
venda_acessorios = 1250.50

receita_total = venda_smartphones + venda_acessorios

print(f"Receita total: R${receita_total:.2f}")


# ---------------------------------------------------------------
# Exercício 9 – Operações de Subtração de Saldo
# O setor de contas a pagar de uma loja precisa calcular o saldo
# disponível após o pagamento de uma fatura de fornecedor.
#
# Tarefa: Crie saldo_atual = 10000 e valor_fatura = 3500.
# Calcule saldo_final e exiba o valor.
# ---------------------------------------------------------------

saldo_atual = 10000
valor_fatura = 3500

saldo_final = saldo_atual - valor_fatura

print(f"Saldo final após o pagamento: R${saldo_final:.2f}")


# ---------------------------------------------------------------
# Exercício 10 – Multiplicação e Divisão de Preços
# Um supermercado vende fardos de produtos e o gerente precisa saber
# o preço unitário para etiquetagem.
#
# Tarefa: Defina preco_fardo = 24.0 e unidades = 6.
# Calcule preco_unitario e exiba o resultado.
# ---------------------------------------------------------------

preco_fardo = 24.0
unidades = 6

preco_unitario = preco_fardo / unidades

print(f"Preço por unidade: R${preco_unitario:.2f}")


# ---------------------------------------------------------------
# Exercício 11 – Otimização de Carga e Estabilidade de Frete
# Um operador logístico trabalha com transporte de insumos industriais.
# Cada saca pesa 65kg e o veículo possui limite de carga útil de 550kg.
#
# Tarefa: Calcule o número máximo de sacas que podem ser embarcadas
# sem exceder o limite e a porcentagem de ocupação do caminhão.
# ---------------------------------------------------------------

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


# ---------------------------------------------------------------
# Exercício 12 – Sincronização de Turnos e Manutenção Preventiva
# Uma planta petroquímica opera em ciclos de 8 dias. Após 125 dias,
# o engenheiro precisa identificar em qual estágio do ciclo a planta
# se encontra para agendar uma parada técnica.
#
# Tarefa: Determine a fase atual do ciclo e quantos dias até a parada.
# ---------------------------------------------------------------

dias_decorridos = 125
periodicidade = 8

dia_atual_do_ciclo = dias_decorridos % periodicidade
dias_faltando = periodicidade - dia_atual_do_ciclo
dias_totais_parada = dias_decorridos + dias_faltando

print(f"Dia atual dentro do ciclo: {dia_atual_do_ciclo}")
print(f"Dias restantes para o fim do ciclo: {dias_faltando}")
print(f"Parada técnica prevista para o dia: {dias_totais_parada}")


# ---------------------------------------------------------------
# Exercício 13 – Engenharia Reversa de Tributação e Logística
# Um analista financeiro precisa calcular o custo de uma licença de
# software (R$2500) com alíquota de 5% e taxa de suporte de R$150,
# onde o suporte não sofre incidência tributária.
#
# Tarefa: Calcule em uma linha o valor final usando parênteses.
# ---------------------------------------------------------------

custo_base = 2500
aliquota = 0.05
suporte = 150

print(f"Valor final: R${custo_base + (custo_base * aliquota) + suporte:.2f}")


# ---------------------------------------------------------------
# Exercício 14 – Auditoria de Desempenho e Eficiência de Ativos
# O gestor de um parque industrial monitora tempo de uso de braços
# robóticos em minutos para calcular custo de depreciação.
#
# Tarefa: Converta 345 minutos para horas decimais e exiba o resultado.
# ---------------------------------------------------------------

minutos = 345
horas = minutos / 60

print(f"O valor convertido: {horas:.2f} h")


# ---------------------------------------------------------------
# Exercício 15 – Telemetria Aeroespacial e Autonomia de Voo
# Um drone realizou dois voos: 3.77 horas e 214 minutos. O sistema
# processa energia em segundos (2.7 joules/segundo) com 15% de margem.
#
# Tarefa: Calcule o total em segundos e a energia necessária com segurança.
# ---------------------------------------------------------------

segundos_voo1 = 3.77 * 3600
segundos_voo2 = 214 * 60
segundos_totais = segundos_voo1 + segundos_voo2
energia = segundos_totais * 2.7
energia_final = energia * 1.15

print(f"Tempo total em segundos: {segundos_totais:.2f}s")
print(f"Energia necessária com segurança: {energia_final:.2f} J")


# ---------------------------------------------------------------
# Exercício 16 – Decomposição de Jornada para Fechamento de Folha
# Um técnico de som trabalhou 1527 minutos. O RH precisa discriminar
# horas completas (R$60,00/h) e minutos excedentes (R$1,20/min).
#
# Tarefa: Calcule horas, minutos excedentes e valores a pagar.
# ---------------------------------------------------------------

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
