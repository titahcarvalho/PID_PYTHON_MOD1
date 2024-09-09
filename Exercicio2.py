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
