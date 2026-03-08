# =============================================================
# Teste de Performance 2 — Introdução à Programação com Python
# Instituto Infnet — Bloco 01
# Adryan Da Silva Santos
# Aproveitamento: 75%
# =============================================================


# ---------------------------------------------------------------
# Exercício 1 – Cabeçalho Multilinha
# A empresa TechSolutions deseja padronizar a documentação inicial
# de seus scripts com um cabeçalho descritivo organizado como bloco
# de texto multilinha.
#
# Tarefa: Armazene em uma única variável string um cabeçalho com:
# Nome do módulo, Data de criação e Descrição — preservando quebras de linha.
# ---------------------------------------------------------------

cabecalho = '''Nome do módulo: Módulo de Vendas Diretas
Data de criação: 15/03/2024
Descrição: Responsável pelo registro e acompanhamento das vendas da equipe externa..'''
print(cabecalho)


# ---------------------------------------------------------------
# Exercício 2 – Geração de SKU
# A equipe de estoque de uma loja de varejo precisa gerar códigos
# de produto (SKUs) combinando prefixo de categoria e número de série.
#
# Tarefa: Combine prefixo e numero_serie para gerar e exibir o SKU completo.
# ---------------------------------------------------------------

prefixo = 'ELT'
numero_serie = '12345'
sku = prefixo + numero_serie
print(f"Seu código SKU é: {sku}")


# ---------------------------------------------------------------
# Exercício 3 – Linha de Separação para Relatórios
# Um analista de dados precisa de separadores visuais padronizados
# entre seções de relatórios de performance de campanhas.
#
# Tarefa: A partir de um caractere e um comprimento, gere uma linha
# de separação com exatamente aquele número de caracteres.
# ---------------------------------------------------------------

caractere = '-'
repeticoes = 30

print(caractere * repeticoes)


# ---------------------------------------------------------------
# Exercício 4 – Mensagem Recebida e Capitalização Invertida
# Educadores desejam um programa interativo que capture uma mensagem
# do aluno e exiba a versão original e a versão com capitalização invertida.
#
# Tarefa: Capture mensagem com input(), exiba confirmação de recebimento
# e a mensagem com swapcase().
# ---------------------------------------------------------------

mensagem = input("Digite uma mensagem: ")
print("Sua mensagem '{}' foi recebida com sucesso".format(mensagem))
print(mensagem.swapcase())


# ---------------------------------------------------------------
# Exercício 5 – Formatação de Nomes para Crachás
# O RH precisa padronizar nomes de colaboradores: nome completo em
# maiúsculas para o sistema interno e nome do crachá com capitalize().
#
# Tarefa: Receba nome_completo e nome_cracha via input(), formate
# e exiba as três versões: completo, crachá e string de segurança.
# ---------------------------------------------------------------

nome_completo = input("Digite o nome completo: ").upper()
nome_cracha = input("Digite o nome para o crachá: ").capitalize()

seguranca = nome_cracha + "---" + nome_completo

print(nome_completo)
print(nome_cracha)
print(seguranca)


# ---------------------------------------------------------------
# Exercício 6 – Verificador de Conformidade de Senha
# A empresa SecureNet precisa verificar se senhas atendem requisitos
# de segurança: presença de @, ! e #, e verificação de maiúsculas/minúsculas.
#
# Tarefa: Verifique cada critério com operador in e métodos isupper/islower,
# armazene em variáveis distintas e exiba os resultados.
# ---------------------------------------------------------------

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


# ---------------------------------------------------------------
# Exercício 7 – Verificador de Limite de SMS
# A empresa Voz Digital precisa garantir que mensagens SMS com prefixo
# e sufixo padrão não ultrapassem 160 caracteres.
#
# Tarefa: Calcule o tamanho total da mensagem final e a diferença
# em relação ao limite de 160 caracteres.
# ---------------------------------------------------------------

mensagem_candidata = 'Desconto exclusivo para você! Válido por tempo limitado.'
prefixo_padrao = 'Voz Digital: '
sufixo_padrao = ' Acesse nosso site para detalhes.'

mensagem = prefixo_padrao + mensagem_candidata + sufixo_padrao
tamanho_total = len(mensagem)
diferenca_limite = 160 - tamanho_total

print(f"O tamanho total da mensagem é de {tamanho_total} caracteres.")
print(f"A diferença em relação ao limite de 160 caracteres é de {diferenca_limite} caracteres.")


# ---------------------------------------------------------------
# Exercício 8 – Cartão ASCII de Boas-Vindas
# Uma equipe de eventos precisa gerar cartões de boas-vindas em texto
# ASCII usando bordas com o caractere =.
#
# Tarefa: Armazene o cartão em uma variável usando repetição e
# concatenação de strings, depois exiba.
# ---------------------------------------------------------------

cartao = "="*35 + "\n" + "=" + " "*33 + "=" + "\n"  + "=" + " "*33 + "=" + "\n"+ "="*35
print(cartao)


# ---------------------------------------------------------------
# Exercício 9 – Construção de URLs de API
# A LinkManager Solutions precisa padronizar a construção de URLs
# combinando domínio, caminho, identificador e ação.
#
# Tarefa: Monte e exiba a URL completa no formato:
# dominio/caminho/identificador/acao
# ---------------------------------------------------------------

dominio_base = 'api.linkmanager.com'
caminho = 'clientes'
identificador = '123'
acao = 'detalhes'
print(f"A URL gerada foi: {dominio_base}/{caminho}/{identificador}/{acao}")


# ---------------------------------------------------------------
# Exercício 10 – Contagem de Hashtags em Postagens
# A equipe de marketing digital monitora a frequência de hashtags
# com capitalização exata e variações minúsculas em postagens.
#
# Tarefa: Conte e exiba separadamente as ocorrências de
# #PythonChallenge e #pythonchallenge no texto.
# ---------------------------------------------------------------

texto = 'Participe do nosso #PythonChallenge e conquiste prêmios! #pythonchallenge agora mesmo!'

quantidade_exata = texto.count("#PythonChallenge")
quantidade_minuscula = texto.count("#pythonchallenge")

print(f"#PythonChallenge apareceu {quantidade_exata} vez(es) no texto")
print(f"#pythonchallenge apareceu {quantidade_minuscula} vez(es) no texto")


# ---------------------------------------------------------------
# Exercício 11 – Gestão de Estoque após Retirada
# O Sr. João do almoxarifado precisa calcular o saldo de produtos
# após uma transação de saída.
#
# Tarefa: Receba quantidade_total e reducao via input() e exiba
# o saldo restante no formato especificado.
# ---------------------------------------------------------------

quantidade_total = int(input("Qual é a quantidade total do produto? "))
reducao = int(input("Qual é a quantidade que será retirada do produto? "))
estoque = quantidade_total - reducao
print(f"Após a retirada de {reducao} itens, o saldo atual é de {estoque} unidades.")


# ---------------------------------------------------------------
# Exercício 12 – Cálculo de Parcelamento com Juros
# A loja Preço Bom precisa calcular o valor total e parcela mensal
# com juros simples e taxa administrativa.
#
# Tarefa: Receba preco, taxa_juros, meses e taxa_admin via input().
# Calcule valor_com_juros usando juros simples + taxa_admin e exiba
# o total e o valor de cada parcela.
# ---------------------------------------------------------------

preco = float(input("Informe o preço à vista do produto: "))
taxa_juros = float(input("Informe a taxa de juros mensal (ex: 0.02 para 2%): "))
meses = int(input("Informe o número de parcelas: "))
taxa_admin = float(input("Informe a taxa administrativa (ex: 0.05 para 5%): "))

valor_com_juros = preco * (1 + taxa_juros * meses) * (1 + taxa_admin)

print(f"o valor final de seu produto: {valor_com_juros:.2f}")
print(f"O valor de cada parcela: {valor_com_juros/meses:.2f}")


# ---------------------------------------------------------------
# Exercício 13 – Pontuação Final em Arcana Quest ⚠️ INCOMPLETO
# O jogo Arcana Quest calcula pontuação final com bônus por sincronia
# tática, dedução por gasto excessivo e fator de amplificação de maestria.
#
# Tarefa: Receba as pontuações das 3 fases e calcule a pontuação final
# aplicando todas as regras de negócio descritas.
#
# NOTA: A solução entregue realizou apenas a soma simples das fases,
# sem aplicar bônus, dedução e fator de amplificação. Exercício incompleto.
# ---------------------------------------------------------------

fase_exploracao = str(input("Digite a pontução da sua exploração: "))
fase_combate = str(input("Digite a pontução do seu combate: "))
fase_estrategia = str(input("Digite a pontução da sua estrategia: "))

ponto_total = int(fase_exploracao) + int(fase_combate) + int(fase_estrategia)

print(f"Pontuação Final em Arcana Quest: {ponto_total} pontos.")


# ---------------------------------------------------------------
# Exercício 14 – Conversão de Temperatura e IET
# A ClimaTech precisa converter temperaturas Celsius para Fahrenheit
# e calcular o Indicador de Estabilidade Térmica (IET).
#
# Tarefa: Receba temperatura em Celsius via input() e exiba
# Fahrenheit e IET no formato: "fahrenheit; iet"
# ---------------------------------------------------------------

temperatura_celsius = float(input("digite a temperatura em graus: "))

fahrenheit = (temperatura_celsius * 9 / 5) + 32
iet = (temperatura_celsius / 4.0) - (temperatura_celsius * 0.08) + 1.5

print(f"{fahrenheit:.2f}; {iet:.2f}")


# ---------------------------------------------------------------
# Exercício 15 – Porcentagem de Vogais em Mensagem
# A equipe de comunicação digital analisa qualidade textual medindo
# a porcentagem de vogais em mensagens de marketing.
#
# Tarefa: Receba mensagem via input(), conte vogais (maiúsculas e
# minúsculas) e exiba a porcentagem em relação ao total de caracteres.
# ---------------------------------------------------------------

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


# ---------------------------------------------------------------
# Exercício 16 – Log de Transação Financeira
# A TechSolutions precisa gerar mensagens de log padronizadas para
# auditoria de transações financeiras com formato específico.
#
# Tarefa: Receba 7 informações via input() e monte o log no formato:
# [LOG: id] - DATA: data hora | TIPO: tipo {ORIGEM: origem -> DESTINO: destino} VALOR: R$valor;
# ---------------------------------------------------------------

id_transacao = input("informe o id da sua transacao: ")
data = input("informe a data (AAAA-MM-DD): ")
hora = input("Informe a hora (HH:MM:SS): ")
tipo = input("informe o tipo DEB (débito) ou CRED (crédito): ")
conta_origem = input("Informe o numero da conta de origem: ")
conta_destino = input("Informe o numero da conta de destino: ")
valor = input("informe o valor da transferencia: ")

log = f"[LOG: {id_transacao}] - DATA: {data} {hora} | TIPO: {tipo} {{ORIGEM: {conta_origem} -> DESTINO: {conta_destino}}} VALOR: R${valor};"
print(log)
