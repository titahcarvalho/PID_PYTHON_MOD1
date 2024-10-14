# funções : Definicao de Funcoes
# Uma funcao e um bloco de codigo que executa uma tarefa especifica. Funcoes ajudam a modularizar o
# código, tornando-o mais legível e reutilizável. Para definir uma funcao em Python, utilizamos a palavra
# chave def, seguida pelo nome da funcao e os parametros entre parenteses.

def soma(a, b):
    """Esta funcao retorna a soma de dois numeros."""
    return a + b


resultado = soma(5, 3)
print("A soma é:", resultado)


# funções com valores padrão
def saudacao(nome="Mundo"):
    """esta funcao imprime uma saudacao"""
    print(f"Olá, {nome}!")


saudacao()  # usara o valor padrão
saudacao("João")  # usará o argumento fornecido


# chamada das funções
def soma(a, b):
    """
    Esta funcão recebe dois numeros e retorna sua soma.
    Parametros:
    a(int ou float): O primeiro numero a ser somado.
    b(int ou float): O segundo numero a ser somado.

    Retorna:
    int ou float: A soma de a e b.
    """
    return a + b


# chamada da função
resultado = soma(5, 3)

# impressão do resultado
print("A soma é:", resultado)


# retorno de valores

def potencia(base, expoente):
    """Esta função calcula a potência de um número."""
    return base ** expoente


resultado = potencia(2, 3)
print("2 elevado a 3 é:", resultado)


def imprimir_mensagem(mensagem):
    """Esta funcão imprime uma mensagem no console."""
    print(mensagem)


imprimir_mensagem("Olá, mundo!")


# EXERCÍCIOS MÓDULO 7 - FUNÇÕES

# Exercício 1: Soma de Números Crie uma função chamada soma que receba dois números como
# argumentos e retorne a soma deles. Teste a função com números diferentes.
def soma(numero1, numero2):
    return numero1 + numero2


resultado = soma(9, 8)
print("9+8 =", resultado)


# Exercício 2: Média de uma Lista Escreva uma função chamada media que receba uma lista de
# números e retorne a média dos valores. Utilize a função para calcular a média de uma lista de cinco
# números.
def media(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5) / 2


media_total = media(4, 6, 7, 3, 5)
print("A média é:", media_total)


# Exercício 3: Verificação de Par ou Ímpar Desenvolva uma função chamada par_ou_impar que
# receba um número e retorne "Par" se o número for par e "Ímpar" se for ímpar. Teste a função com
# diferentes números.
def par_ou_impar(numero):
    if numero % 2 == 0:
        print("é par.")
    else:
        print("é ímpar.")


par_ou_impar(7)


# Exercício 4: Fatorial Crie uma função chamada fatorial que receba um número inteiro e retorne
# o fatorial desse número. Utilize a função para calcular o fatorial de um número de sua escolha.
def fatorial(numero_inteiro):
    if numero_inteiro == 1 or numero_inteiro == 0:
        return 1
    else:
        return numero_inteiro * fatorial(numero_inteiro - 1)


numero_inteiro = 5
resultado = fatorial(numero_inteiro)
print(f"O fatorial de {numero_inteiro} é:", resultado)


# Exercício 5: Potência Escreva uma função chamada potencia que receba dois argumentos, a base
# e o expoente, e retorne a potência da base elevada ao expoente. Teste a função com diferentes
# valores.

def potencia(base, expoente):
    return base ** expoente


base = 7
expoente = 3
resultado = potencia(7, 3)
print("A potência de", {base}, "elevado a", {expoente}, "é:", resultado)


# Exercício 6: Contagem de Vogais Desenvolva uma função chamada contar_vogais que receba uma
# string e retorne o número de vogais presentes na string. Teste a função com uma frase de sua
# escolha.

def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    contagem = 0

    for char in frase:
        if char in vogais:
            contagem += 1

    return contagem


frase = "Eu passei em AEDS"
resultado = contar_vogais(frase)
print(f"O numero total de vogais em {frase} é:", resultado)


# Exercício 7: Palíndromo Crie uma função chamada eh_palindromo que verifique se uma string é
# um palíndromo (ou seja, se a string é igual a ela mesma lida de trás para frente). Teste a função
# com diferentes palavras.
def eh_palindromo(palavra):
    reservado_palavra = ""
    for char in palavra:
        reservado_palavra = char + reservado_palavra
    return reservado_palavra == palavra


# teste da função
resultado = eh_palindromo("arara")
print("é palindromo?", resultado)


# Exercício 8: Fibonacci Escreva uma função chamada fibonacci que receba um número inteiro n e
# retorne uma lista com os n primeiros números da sequência de Fibonacci
def Fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]


# teste da função
resultado = Fibonacci(5)
print("Os 5 primeiros numeros da sequencia Fibonacci são:", resultado)

















