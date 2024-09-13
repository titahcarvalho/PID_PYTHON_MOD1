#ESTRUTURAS CONDICIONAIS

#EXEMPLOS:
idade = 18
if idade >= 18:
print(f"Você é maior de idade")
print(f"Pode entrar na festa")

#verificação de numero par
numero = 10
if numero %2 == 0:
    print(f"{numero} é um número par")

#exemplo de string vazia

nome = " "
if not nome:
    print(f"Por favor insira um nome válido.")

#else - usada quando a condição do if não é verdadeira

#exemplo:
idade = 16
if idade >= 18:
    print(f"Você é maior de idade")
    print(f"Pode entrar na festa")
else:
    print(f"Você é MENOR de idade")
    print(f"NÃO Pode entrar na festa")

usuario = "admin"
senha = "senha123"

if usuario == "admin" and "senha" == "senha123":
    print(f"Login bem-sucecido!")
else:
    print(f"Usuario ou senha incorretos.")

#exemplo verificação de numero positivo ou negativo

numero = -5
if numero >= 0:
    print(f"{numero} e positivo ou zero")
else:
    print(f"{numero} e negativo.")

#ESTRUTURA ELIF - QUANDO HÁ VÁRIAS ALTERNATIVAS POSSÍVEIS
#exemplo:
nota = 75
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")
#EXEMPLO CATEGORIAS DE IMC
imc = 27.5
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obesidade grau 1")
elif 35 <= imc < 40:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")

#EXEMPLO DIAS DA SEMANA
dia = 3
if dia == 1:
    print("Segunda-feira")
elif dia == 2:
    print("Terça-feira")
elif dia == 3:
    print("Quarta-feira")
elif dia == 4:
    print("Quinta-feira")
elif dia == 5:
    print("Sexta-feira")
elif dia == 6:
    print(" Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("Dia inválido")

#COMBINANDO ESTRUTURAS CONDICIONAIS
idade = 25
membro = True
compra = 150
if idade >= 60:
    if membro:
        desconto = 0.20 #20% de desconto
    else:
        desconto = 0.15
elif membro:
    if compra >= 100:
        desconto = 0.10
    else:
        desconto = 0.05
else:
    desconto = 0
valor_final = compra *(1-desconto)
print(f"Valor final da compra: R${valor_final:.2f}")

#OPERADORES LOGICOS EM CONDIÇÕES - AND OR NOT JUNTO A CONDICIONAIS
#EXEMPLO VERIFICAÇÃO DE ELEGIBILIDADE PARA EMPRESTIMO
idade = 30
renda = 500
score_credito = 700

if (idade >= 21 and idade <= 65) and (renda >= 3000) and (score_credito >= 650):
    print(f"Eleegível para empréstimo.")
elif idade < 21 or idade > 65:
    print(f"Idade fora da faixa permitida")
elif renda < 3000:
    print("Renda insuficiente")
else:
    print("Score de credito baixo")

#ESTRUTURA MATCH-CASE (PYTHON 3.10+) SIMILAR OU SWITCH - CASE
#Exemplo dias da semana
dia = 3
match dia:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-feira")
    case 4:
        print("Quinta-feira")
    case 5:
        print("Sexta-feira")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Dia inválido")

#exemplo tipos de dados
def tipo_dado(valor):
    match valor:
        case int():
            print("E um inteiro")
        case float():
            print("É um numero de ponto flutuante")
        case str():
            print("É uma string")
        case list():
            print("É uma lista")
        case dict():
            print("É um dicionário")
        case _:
            print("Tipo não reconhecido")
tipo_dado(42)
tipo_dado("Python")
tipo_dado([1,2,3])

#exemplo padrões complexos
def analisar_ponto(ponto):
    match ponto:
        case(0,0):
            print("Origem")
        case(0, y):
            print(f"No eixo Y, y = {y}")
        case(x,0):
            print(f"No eixo X, x = {x}")
        case(x,y) if x == y:
            print(f"Na diagonal, x=y={x}")
        case(x,y):
            print(f"Ponto genérico({x},{y})")
        case _:
            print(f"Não é um ponto válido")
analisar_ponto((0,0))
analisar_ponto((0,5))
analisar_ponto((3,3))
analisar_ponto((2,4))

# exercícios práticos
# 1  1. Escreva um programa que solicite a idade do usuario e imprima se ele pode ou nao votar (a idade minima para votar e 16 anos).
idade = int(input("Digite a sua idade:"))
if idade >= 16:
    print(f"Hábil a votação.")
else:
    print("Você ainda não possui a idade mínima para votar.")
# 2. Crie um programa que calcule o IMC (Indice de Massa Corporal) de uma pessoa e classifique o resultado em: Abaixo do peso, Peso normal, Sobrepeso ou Obeso.
peso = float(input("Digite o seu peso em kg:"))
altura = float(input("Digite a sua altura em metros:"))
imc = peso / (altura ** 2)
if imc < 18:
    print("Você está abaixo do peso")
elif 18 <= imc < 25:
    print("Você está com o peso normal")
elif 25 <= imc < 30:
    print("Você está com sobrepeso")
else:
    print("Você está obeso")
#  3.Desenvolva um programa que solicite tres numeros ao usuario e imprima o maior deles.
numero1 = int(input("Digite o primeiro numero:"))
numero2 = int(input("Digite o segundo numero:"))
numero3 = int(input("Digite o terceiro numero:"))

if (numero1 > numero2) and (numero1 > numero3):
    print(f"O {numero1} é maior.")
elif (numero2 > numero1) and (numero2 > numero3):
    print(f"O {numero2} é maior.")
else:
    print(f"O {numero3} é maior.")

# 4. Implemente um programa que determine se um ano fornecido pelo usuario e bissexto ou nao.
ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 != 0:
        print(f"O {ano} NÃO é bissexto")
    else:
        print(f"{ano} É bissexto")
else:
    print("O {ano} não é bissexto")

    # 5. Crie um programa que simule um sistema de notas escolar, onde o usuario insere uma nota de 0 a 100 e o programa retorna o conceito correspondente (A, B, C, D ou F).
    nota = float(input("Insira a nota:"))
    if nota > 90:
        print("A")
    elif nota >= 80:
        print("B")
    elif nota >= 70:
        print("C")
    elif nota >= 60:
        print("D")
    else:
        print("F")

    # Desenvolva um programa que simule um caixa eletronico. O programa deve perguntar o valor do
    # saque e informar quantas notas de cada valor serao fornecidas, considerando que ha notas de R100,R 50,
    # R20eR 10.
    valor = float(input("Digite um valor de saque:"))

    nota100 = valor // 100
    valor = valor % 100

    nota50 = valor // 50
    valor = valor % 50

    nota20 = valor // 20
    valor = valor % 20

    nota10 = valor // 10
    valor = valor % 10

    nota5 = valor // 5
    valor = valor % 5

    moeda1 = valor // 1
    valor = valor % 1

    moeda50 = valor // 0.50
    valor = valor % 0.5

    print(f"As notas disponiveis para o saque são:")
    print(f"Nota de $100: {nota100}")
    print(f"Nota de $50: {nota50}")
    print(f"Nota de $20: {nota20}")
    print(f"Nota de $10: {nota10}")
    print(f"Nota de $5: {nota5}")
    print(f"Moeda de $1: {moeda1}")
    print(f"Moeda de $0,50: {moeda50}")






