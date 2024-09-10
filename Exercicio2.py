# 1. Crie um programa que solicite o nome, idade e cidade do usuário, e então imprima uma mensagem formatada com essas informações.

nome = input("Qual é o seu nome:")
idade = int(input("Qual é a sua idade?"))
cidade = input("Qual é a sua cidade?")

print(f"O seu nome é {nome} \nA sua idade é {idade} \nA sua cidade é {cidade}")

# 2. Desenvolva uma calculadora de IMC (Índice de Massa Corporal). Peça ao usuário sua altura em metros e peso em quilogramas, calcule o IMC e imprima o resultado com duas casas decimais.

print(f" ----- Vamos calcular o seu IMC -----")
altura = float(input("Digite a sua altura em metros:"))
peso = float(input("Digite o seu peso em gramas:"))

imc = (peso/altura**2)
print(f" O seu IMC é: {imc:.2f}")

#3 Desenvolva um programa que peça ao usuário para inserir uma frase e
 #então imprima:- A frase em maiúsculas- A frase em minúsculas- O número
 #de caracteres na frase- A frase com cada palavra capitalizada

frase = input("Digite uma frase: ")

print(f"Frase em maiúsculas: {frase.upper()}")

print(f"Frase em minúsculas: {frase.lower()}")

print(f"Número de caracteres na frase: {len(frase)}")

print(f"Frase com cada palavra capitalizada: {frase.title()}")

#EXERCÍCIOS MÓDULO 4
#FaÇa um programa que solicite o ano de nascimento do usu´ario e calcule sua idade (considere o ano atual como 2023)
ano_nascimento = int(input("Digite o ano de seu nascimento:"))
idade = 2024 - ano_nascimento
print(f"Você tem {idade}anos.")

# Escreva um programa que pe¸ ca o raio de um c´ırculo ao usu´ario e imprima sua ´area (use pi = 3.14159).
raio = float(input("Digite o raio de uma circuferencia em cm:"))
pi = 3.14159
area = pi*(raio**2)
print(f"A area dessa circuferencia é: {area}")

#Faça um programa que solicite um número inteiro e imprima seu antecessor e seu sucessor.
numero = int(input("Digite um número:"))
ant = numero - 1
suc = numero + 1
print("O antecessor de", numero,"é:",ant, "\nO sucessor de", numero,"é:", suc)
#10. Escreva um programa que pe¸ ca o sal´ario base de um funcion´ario e calculeo sal´ario l´ ıquido, considerando um desconto de 10% para impostos.
salario = float(input("Digite o seu salario bruto:"))
liquido = salario - (salario * 0.1)

print(f"O seu salario liquido é: R${liquido:.2f}")
