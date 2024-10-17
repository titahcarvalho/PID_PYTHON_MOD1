#LISTASSS
#criando uma lista de números
numeros = [1,2,3,4,5]

#crianco uma lista de strings
frutas = ["maca","banana", "pera"]

#listas com diferentes tipos de dados
mistura = [1,"dois", 3.0,True]

#ACESSANDO ELEMENTOS

frutas = ["maca","banana", "pera"]

print(frutas[0])
print(frutas[1])
print(frutas[-1]) #pera, último ELEMENTOS

#OPERAÇÕES COM listas
numeros = [1,2,3]
numeros.append(4)  #adiciona ao final da lista
print(numeros) #saida: [1,2,3,4]

numeros.insert(1,1.5) #insere 1.5 na posição 1
print(numeros)

numeros.extend([5,6]) #adicona multiplos ELEMENTOS
print(numeros) #saída[1,1.5,2,3,4,5,6]

#REMOVENDO ELEMENTOS

frutas = ["maca","banana","laranja","uva"]
frutas.remove("banana") #remove a primeira ocorrencia de banana
print(frutas) #saida maca, laranja uva

ultimo = frutas.pop() #remove e retorna o ultimo ELEMENTO
print(ultimo) #saida uva
print(frutas) #saida: maca,laranja


del frutas[0] #remover o elemento no indice 0
print(frutas) #saida laranja

#ORDENAÇÃO DE listas

numeros = [3,1,4,5,9,2,6,5,3,5]
numeros.sort() #ordena a lista in-place
print(numeros) #saida: [1,1,2,3,3,4,5,5,6,9]

numeros.sort(reverse=True) #ordena em ordem decrescente
print(numeros) #saida: [9,6,5,5,4,3,3,2,1,1]

frutas = ["banana","maca", "laranja"]
frutas_ordenadas = sorted(frutas) #retorna uma nova lista frutas_ordenada
print(frutas_ordenadas) #saida : banana,laranja, maca


#OPERAÇÕES AVANÇADAS COM LISTAS

#concatenação de listas
lista1 = [1,2,3]
lista2 = [4,5,6]
concatenada = lista1 + lista2
print(concatenada) #saida: [1,2,3,4,5,6]

#multiplicação de listas
repetida = [0] * 5
print(repetida) #[0,0,0,0,0]

#compreensão de listas
quadrados = [x**2 for x in range(1,6)]
print(quadrados) #[1,4,9,16,25]

#filtragem com compreensão de lista
pares = [x for x in range(10) if x % 2 == 0]
print(pares) #[0,2,4,6,8]

#MÉTODOS DE LISTAS
numeros = [1,2,3,2,4,2,5]
print(len(numeros)) #saida: 7 (comprimento da lista)
print(numeros.count(2)) #saida: 3 (conta ocorrencias de 2)
print(numeros.index(4)) #saida: 4 (indice do primeiro 4)

numeros.reverse() #inverter a ordem dos ELEMENTOS
print(numeros) #saida[5,2,4,2,3,2,1]

copia = numeros.copy() #cria uma copia superficial da lista
print(copia) #saida: [5,2,4,2,3,2,1]

#LISTAS COMO PILHA E FILAS
#usando lista como pilha (LIFO)

pilha = []
pilha.append(1) #append empilha nesse caso
pilha.append(2)
pilha.append(3)
print(pilha.pop()) #tira o 3
print(pilha.pop()) #tira o 2
print(pilha) #fica o 1

#usando lista como fila(FIFO)
from collections import deque
fila = deque(["Eric", "Joao", "Micael"])
fila.append("Tereza") #append adiciona nesse caso
print(fila.popleft()) #Eric saiu, mas é impresso por ter sido o primeiro a entrar
print(fila)  #deque(['joão, micaelm tereza'])
print(fila.popleft()) #joao saiu
print(fila)
fila.append("Angelica") #entra Angelica
print(fila)

#OPERAÇÕES COM MATRIZES(LISTA DE LISTAS)

#criando uma matriz 3por3
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#ACESSANDO ELEMENTOS DA matriz
print(matriz[1][1]) #5
print(matriz[2][2])  #6?, não 9
print(matriz[0][2]) # creio q seja o 3, isso. começa em 0,1,2

#TRANSPOSTA DA matriz
transposta = [[linha[i] for linha in matriz] for i in range(3)]
print(transposta) #[[1,4,7],[2,5,8],[3,6,9]]

#SOMANDO TODOS OS ELEMENTOS DA matriz

soma = sum(sum(linha) for linha in matriz)
print(soma) #45





























