# EXERCÍCIOS MODULO 2

idade = 27
print(idade)
nome = "Angélica de Carvalho Teixeira"
print(nome)
altura = 1.75
is_estudante = True
print(altura)
print(is_estudante)
print(type(idade))
print(type(nome))
print(type(altura))
print(type(is_estudante))

peso = 58.4
cidade_natal = "São Gonçalo do Rio Abaixo"
temperatura = 24
possui_animal_estimacao = True
pi = 3.141592

print(peso)
print(cidade_natal)
print(temperatura)
print(possui_animal_estimacao)
print(pi)

# EXERCÍCIOS MODULO 3
#1. Calcule a area de um circulo dado o raio.
#a=pi*r² = formula
import math
p = math.pi
r = 3
area = p*(r**2)
print(f"Area: {area}" )

#2. Crie uma funcao que verifica se uma palavra e um palindromo.

def palindromo(palavra):
    # Converte a palavra para minúsculas para ignorar a diferença entre maiúsculas e minúsculas
    palavra = palavra.lower()

    if palavra == palavra[::-1]:
        print(f"A palavra {palavra}: é um palindromo")
    else:
        print(f"A palavra {palavra}: não um palindromo")
palavra = "Ana"
palindromo(palavra)

# 3. Implemente um conversor de temperatura de Celsius para Fahrenheit.
temperaturaCelsius = 35
temperaturaFah = (temperaturaCelsius * 1.8) + 32
print( f"A temperatura em Celcius de {temperaturaCelsius} convertida para Fahrenheit é: {temperaturaFah}")
print(f"A temperatura em Fahrenheit de {temperaturaFah} convertida para Celsiu é: {temperaturaCelsius}")

#4. Crie um programa que determine se um ano e bissexto.
#Um ano é bissexto se for divisível por 4.
#Entretanto, se o ano for divisível por 100, ele só será bissexto se também for divisível por 400

def ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0 and ano % 400 != 0:
            print(f"O {ano} não é bissexto")
        else:
            print(f"O {ano} é bissexto")

    else:
        print(f"O {ano} não é bissexto")

ano = 2048
ano_bissexto(ano)


