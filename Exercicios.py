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

#--------------------------------------
# 1. Crie duas variáveis numéricas e realize as quatro operacoes básicas (adição,
#subtração, multiplicação e divisão) entre elas.
a = 9
b = 8
m = a * b
s = a + b
sub = a - b
d = a // b

print( m, s , sub, d)

#2. Calcule o resto da divisão de 17 por 3 usando o operador de módulo.
a = 17
b = 3
div = a % 3
print(div)

# 3. Crie uma expressão que verifica se um número é par. Use o operador de
#módulo e o operador de igualdade.
a = 654
if( a % 2 == 0):
    print(f"O numero é par")
else:
    print(f"O numero não é par")

# 4. Declare duas variáveis booleanas e use os operadores lógicos AND e OR
#para combinar seus valores.

a = True
b = False

print(a and b)
print(a or b)
print(not b)

#5. Crie uma expressão que verifica se um número está entre 0 e 100 (inclu
#sive). Use os operadores de comparação e o operador lógico AND.

a = 93

if (a <=  100 and a >= 0): # poderia usar o &&? não, somente em outras linguagens como C que é utilizado, em python não usa o && como and
    print(f"O número é menor que 100 e maior que 0")

else:
    print(f"O número não está entre 0 e 100")

# 6. Calcule a média de três números usando operadores aritméticos

a = 1
b = 2
c = 3
media = a + b + c / 2
print(media)

#7. Crie uma expressão que verifica se um ano é bissexto (divisível por 4, mas
#não por 100, a menos que seja divisível por 400).

def anobissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0 and ano % 400 != 0:
            print(f"O {ano} não é bissexto")
        else:
            print(f"O {ano} é bissexto")
    else:
        print(f"O {ano} não é bissexto")

    ano = 2048
    anobissexto(ano)

# 8. Use o operador de exponenciação para calcular 2 elevado a 10ª potência

a = 2 ** 10
print(a)

#9. Crie uma expressão que verifica se um número é múltiplo de 3 e de 5 ao mesmo tempo.
a = 20
if a % 3 == 0 and a % 5 == 0:
    print(f"Esse número é múltiplo de 3 e 5 ao mesmo tempo")
elif a % 3 == 0:
    print(f"Esse número é multiplo apenas de 3 ")
elif a % 5 == 0:
    print(f"Esse número é múltiplo apenas de 5 ")
else:
    print(f"Esse número não é múltiplo de 3 e nem de 5 ao mesmo tempo")

#10. Use o operador de divisão inteira para calcular quantas horas completas
# há em 1000 minutos.

minutos = 1000
divi = minutos // 60
print(f"Em {minutos} minutos há {divi} horas")

