#LAÇO FOR:

#for variável in sequencia:

numeros = [1,2,3,4,5]

for numero in numeros:
    print(numero)

#exemplo 2 usando range()
for i in range(1,6):
    print(i)

#exemplo 3 interando sobre uma string
palavra = "Python"

for letra in palavra:
    print(letra)

#exemplo 4 iterando sobre um dicionario
alunos = {"Ana": 85,"Bruno":92, "Carlos": 78}

for nome, nota in alunos.items():
    print(f"{nome}:{nota}")

#laço while
#while condicao:
    #bloco de código

#exemplo 5 - contagem regressiva
contador = 5
while contador > 0:
    print(contador)
    contador -= 1

#exemplo 6 laço while com condição de saída
numero_secreto = 7
palpite = 0
while palpite != numero_secreto:
    palpite = int(input("Adivinhe o numero:"))
print("Parabéns! Você acertou.")

#exemplo 7: evitand loops infinitos - usar break
contador = 10
while contador > 0:
    print(contador)
    contador -= 1
    if contador == 2:
        break# Saindo do loop antecipadamente
 #É como se você estivesse descendo uma escada e, de repente, decide parar
 #no segundo degrau.
#exemplo 8 criando um iterador
frutas = [ 'maça', 'banana', 'cereja']
iterador = iter(frutas)

print(next(iterador))
print(next(iterador))
print(next(iterador))

#usando iteradores com for
frutas = ['maça','banana','cereja']
for fruta in frutas:
    print(fruta)

#exemplo 10 iteradres infinitos com itertools
import itertools
contador = itertools.count(start = 1, step = 2)

for i in range(5):
    print(next(contador)) #saida: 1,3,5,7,9

#EXERCICIOS PRÁTICOS

#. 1) Escreva um código que utilize um laço for para imprimir todos os números pares de 1 a 20.
for num in range (1, 21, ):
    print (num)
#Crie um programa que use um laço while para solicitar ao usuário que adivinhe um número secreto até que ele acerte.
num_advinhar = int(input(("Digite um número para o seu amigo adivinhar:")))
palpite = 0

while palpite != num_advinhar:
    palpite = int(input("Adivinhe o número que o seu amigo digitou anteriormente:"))
print(f"Parabéns. Você adivinhou o número {num_advinhar}!")

#Utilize um for para iterar sobre um dicionário e imprimir suas chaves e valores.
lista = {'Abacate': 2,'Limão': 4, 'Alho':8, 'Cebola':9}

for item, quant in lista.items():
    print(f"{item}: {quant}")

# Escreva um código que converta uma lista de strings em uma lista de inteiros, utilizando um laço for.
# imprimir numeros ímpares de 1 a 20

for numero in range(1, 21):
    if numero % 2 == 1:
        print(numero)

# Usandoomóduloitertools, crie umiterador infinito que gere números
# pares e imprima os primeiros 10 números gerados

frutas = ['maça', 'banana', 'uva']
iterador = iter(frutas)

print(next(iterador))
print(next(iterador))
print(next(iterador))

# usando for ...
frutas = ['maça', 'banana', 'uva']
for frutas in frutas:
    print(frutas)

import itertools

interador_infinito = itertools.count(start=0, step=2)

for pares in range(10):
    print(next(interador_infinito))

# Imprimir números ímpares de 1 a 20.

for impares in range(1, 21):
    if impares % 2 == 1:
        print(impares)

# imprimir lista de frutas:

frutas = ['abacate', 'maça', 'melão']
for fruta in frutas:
    print(fruta)

# Contagem at´e um n´ umero fornecido pelo usu´ario.

numero = int(input("Digite um numero:"))

while numero > 0:
    print(numero)
    numero -= 1

# Imprimir pa´ ıses e capitais.
paises = {"Argentina": "Buenos Aires", "Brasil": "Brasilia", "Canadá": "Ottawa"}

for pais, capital in paises.items():
    print(f"{pais}: {capital}")
# Contagem regressiva de 10 a 1.

numero = 10
while numero > 0:
    print(numero)
    numero -= 1
# -------------------------------------
for num in range(10, 0, -1):
    print(num)

# 6. Calcular soma dos n´ umeros em uma lista.

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
for num in numero:
    soma += num
print(f"{numero}")
print(f"A soma é {soma}")

# Imprimir letras de uma palavra até encontrar ’a’:

palavra = input("Digite uma palavra:")
i = 0
while i < len(palavra):
    if palavra[i] == 'a':
        break
    print(palavra[i])
    i += 1

# Imprimir a tabuada do 7:
for i in range(1, 11):
    print(f"7 X {i} = {7 * i}")

# Criar nova lista com números pares:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in numeros if num % 2 == 0]
print(pares)

# Gerar sequência Fibonacci até um número maior que 100:
a, b = 0, 1
while a <= 100:
    print(a)
    a, b = b, a + b

























