# ESCOPO DE VARIÁVEIS
# ESCOPO local
def funcao_exemplo():
    x = 10  # variavel local
    print(f"Dentro da função x = {x}")


funcao_exemplo()  # imprime: dentro da função: x = 10


# print(x) #gera um NameError: name 'x' is no defined

# FUNÇÕES ANINHADAS

def funcao_externa():
    y = 20

    def funcao_interna():
        print(f"Acessando y de dentro: {y}")

    funcao_interna()
    # print(z) #geraria um erro, z não esta definido aqui


funcao_externa()

# ESCOPO GLOBAL
contador_global = 0


def incrementa_contador():
    global contador_global
    contador_global += 1
    print(f"Contador: {contador_global}")


incrementa_contador()  # imprime: contador: 1
incrementa_contador()  # imprime: contador: 2

print(f"Valor final: {contador_global}")  # imprime valor final: 2

# A PALAVRA CHAVE GLOBAL

x = 10


def modifica_x():
    global x
    x = 20


print(f"Antes: {x}")  # imprime o valor de x antes:10
modifica_x()
print(f"Depois: {x}")  # imprime o valor de x depois: 20


# PALAVRA NONLOCAL
def contador():
    count = 0

    def incrementa():
        nonlocal count
        count += 1
        return count

    return incrementa


c = contador()
print(c())  # imprime 1
print(c())  # imprime 2
print(c())  # imprime 3


# ARGUMENTOS DE FUNÇÕES
# ARGUMENTOS POSICIONAIS
def calcula_media(a, b, c):
    return (a + b + c) / 3


media = calcula_media(7, 8, 9)
print(f"Media: {media}")  # Imprime: Media: 8.0


# ARGUMENTOS PADRÃO

def potencia(base, expoente=2):
    return base ** expoente


print(potencia(3))  # imprime: 9 (3^2)
print(potencia(3, 3))  # imprime: 27 (3^3)


# ARGUMENTOS PALAVRAS-CHAVES

def cria_perfil(nome, idade, profissao="Estudante"):
    return f"Nome:{nome}, \nIdade:{idade}, \nProfissão:{profissao}"


print(cria_perfil("Ana", 25))
# imprime: Nome: Ana, Idade 25, Profissoaa: Estudante

print(cria_perfil(idade=30, nome="Carlos", profissao="Engenheiro."))


# imprime: Nome: Carlos, Idade: 30, Profissão: Engenheiro

# NUMERO VARIÁVEL DE ARGUMENTOS

# *ARGS
def soma(*args):
    return sum(args)


print(soma(1, 2, 3))  # imprime: 6
print(soma(1, 2, 3, 4, 5))  # imprime: 15


# **KWARGS

def info_pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


info_pessoa(Nome="Maria", Idade=30, Cidade="São Paulo")


# imprime: nome: Maria, idade: 30, cidade: são paulo

# PASSAGEM DE ARGUMENTOS
def tenta_modificar(x):
    x += 1
    print(f"Dentro da função: {x}")


a = 10
tenta_modificar(a)
print(f"Fora da função: {a}")


# imprime: Dentro da função: 11
# Fora da função: 10


# PASSAGEM POR REFERENCIA
def modifica_lista(lst):
    lst.append(4)
    print(f"Dentro da função: {lst}")


numeros = [1, 2, 3]
modifica_lista(numeros)
print(f"Fora da função: {numeros}")

# imprime: dentro da função: [1,2,3,4]
# fora da função: [1,2,3,4]

# ----------------------- EXERCICIOS ---------------------
# Explique o que acontecerá quando o seguinte código for executado e por quê:
x = 10


def modificar():
    x = 20
    print(f"Dentro da função: {x}")


modificar()
print(f"Fora da função: {x}")

# Resposta:
# Quando o código for executado a função "modificar()" irá receber inicialmente o valor de 20, e imprimir 20
# pois esse valor foi atualizado e modificado dentro da função "modificar()", por outro lado, quando for executado fora da
# fora da função o x irá ser impresso com o valor de 10, por estar fora da função.


# 2.Modifique a função do exercício 1 para que ela altere o valor da variável global x. Escreva o código modificado.
x = 10


def modificar():
    global x
    x = 20
    print(f"Dentro da função: {x}")


modificar()
print(f"Fora da função: {x}")
# ele passa a valer para a parte de fora da função também

# 3. Crie uma função chamada contador que utilize uma variável não local para contar o número de
# vezes que foi chamada. A função deve retornar o número atual de chamadas.

# ERRADO
count = 0


def contador():
    global count
    count += 1
    print(f"Chamada: {count}")


contador()
contador()
contador()


# NONLOCAL
# PALAVRA NONLOCAL
def contador():
    count = 0

    def incrementa():
        nonlocal count
        count += 1
        return count

    return incrementa


c = contador()
print(c())  # imprime 1
print(c())  # imprime 2
print(c())  # imprime 3































