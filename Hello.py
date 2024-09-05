import math
print("helllo, world")

def calcular_area_retangulo(largura, altura):
    area = largura * altura
    return area

#usando a função
largura_retangulo = 5
altura_retangulo = 3
area_retangulo = calcular_area_retangulo(largura_retangulo, altura_retangulo)
print(f"A altura do retangulo é: {area_retangulo}")

#----------------------------------------------------------
#variaveis com diferentes tipos de dados
idade = 27
nome = "Angel"
altura = 1.75
is_estudante = True

#nomes de variaveis validos

_contador = 0
valor_total = 100.50
x1 = 10
Usuario_2 = "Bob"

#nomes de variáveis inválidos (comentados para evitar erros)

#2nome = 'Invalido' #não pode começar com numeros
#meu-nome = 'Invalido' #não pode conter hifen
# for = 5 # não pode ser uma palavra reservada

a,b,c = 1,2,3
x=y=z=0

contador = 0
print(contador) #saida:0

contador = contador+1
print(contador) # saida:1

contador = "Zero"
print(contador) # saida: Zero

 #operadores de atribuição compostos // python oferece operadores que combinam uma operação aritmetica com atribuição
x = 5
x += 3 #equivalente a x = x+3
print(x) #saida:8

y = 10
y *= 2
print(y)

#uso de variaveis em expressoes

#expressoes matematicas

a = 5
b = 3
soma = a + b
diferenca = a -b
produto = a * b
quociente = a / b
potencia = a**b

print ( f" Soma : { soma }")
print ( f" Diferenca : { diferenca }")
print ( f" Produto : { produto }")
print ( f" Quociente : { quociente }")
print ( f" Potencia : { potencia }")

#expressoes com strings

primeiro_nome = "Angélica"
sobrenome = "Carvalho"
nome_completo = "Angélica de Carvalho Teixeira"

idade = 27
mensagem = f"{nome_completo} tem {idade} anos"
print(mensagem)

#expressoes logicas
x = 5
y = 10
maior_que = x > y
menor_que = x < y
igual = x == y

print(f"x é maior que y? {maior_que}")
print(f"x é menor que y? {menor_que}")
print(f"x é igual a y? {igual}")


#escolha de nomes significativos
#bom
idade_usuario = 25
total_vendas = 1000.50

#evitar
a = 25
tv = 1000.50

#uso de snake_case
#recomendado
nome_completo = "Angelica Carvalho"
idade_em_anos = 27

#não recomendado em python
nomeCompleto = "Bob Santos"
idadeEmAnos = 25  #cmo que faço? já tenho o costume de usar camelCase kkkkk


#constantes (variaveis que não devem ser alteradas - use letras maiúsculas
PI = 3.14159
VELOCIDADE_DA_LUZ = 299792458

# Evite abreviações ambiguas - use nomes completos em vez de abreviações que possam ser confusas
#bom
temperatura_maxima = 35.5
velocidade_medica = 60.0

#evitar
temp_max = 35.5
vel_med = 60

#Definição e exemplos de inteiros em python3, não há limites para o tamanho do inteiro

x = 5
y = -10
z = 1000000

a = 10
b = 3
soma = a + b
diferenca = a - b
produto = a * b
quociente = a / b #resulta em float
quociente_inteiro = a // b
resto = a % b
potencia = a ** b

print(f"Soma: {soma}")
print(f"Diferenca: {diferenca}")
print(f"Produto: {produto}")
print(f"Quociente: {quociente}")
print(f"Quociente inteiro: {quociente_inteiro}")
print(f"Resto: {resto}")
print(f"Potencia: {potencia}")


# em python, inteiros tem precisão arbitrária. Isso significa que podem crescer até o limite da memória disponível
# uma peculiaridade importante é a divisão
#divisão normal sempre retorna um FLOAT
print(10/3) # saída: 3.3333
#DIVISÃO inteira retorna um int
print(10//3) # saida: 3


#NÚMEROS DE PONTO FLUTUANTE (FLOAT)
#Float são numeros com componentes fracionários

x = 3.14
y = -0.001
z = 2.5e-4 # notação científica

# Operações com float
a = 3.14
b = 2.10

soma = a + b
diferenca = a - b
produto = a * b
quociente = a / b
potencia = a ** b

print(f"Soma: {soma}")
print(f"Diferenca: {diferenca}")
print(f"Produto: {produto}")
print(f"Quociente: {quociente}")
print(f"Potencia: {potencia}")

#Precisão e Arredondamento
#float têm precisao limitada e podem levar a resultados inesperados em comparações:
print(0.1 + 0.2 == 0.3) # saída: false
print(0.1 + 0.2) #saída: 0.30000000000004

#para lidar com isso, utiliza-se a função round() ou o módulo decimal para cálculos que exigem precisão
from decimal import Decimal
a = Decimal ('0.1')
b = Decimal ('0.2')
print( a + b == Decimal ('0.3')) # saida: true

#strings são sequências imutáveis de caracteres Unicode
nome = "Angel"
frase = 'Python e incrivel!'
texto_longo = """"Este é um texto 
que ocupa multiplas linhas."""

#strings
s1 = 'String com aspas simples'
s2 = "String com aspas duplas"
s3 = '''String com aspas triplas para
multiplas
linhas'''
s4 = """"outra
string 
multilinha"""

#operações básicas com strings
a = "olá"
b = "mundo"

concatencao = a + " " + b
repeticao = a*3, b*4

print(concatencao) # saída olá mundo
print(repeticao) #saida oláoláolá 3 vezes

#strings também suportam indexação e fatiamento:
s = "Python"
print(s[0]) #saída: P
print(s[1:4]) #saída: yth
print (s[::-1]) #saída: nohtyp (INVERTER A STRING)

#booleanos / representam valores de verdade lógica, true ou false
is_python_fun = True
is_coffee_cold = False

x = 5
y = 10
print(x<y)# saida true
print(x == y)# saida false
print( x > 0 and y < 20) #saida true

# função type() retorna o tipo do objeto

x = 5
y = 3.14
z = "Hello"
w = True

print(type(x))
print(type(y))
print(type(z))
print(type(w)) #saida: <class 'bool'>

#conversão de tipos

num_str = "42"
num_int = int(num_str)
num_float = float(num_str)

print(num_int + 8)# saida 50
print(num_float + 0.5) # saida 42.5

#-------------------------------------------------------------------
#OPERAÇÕES MATEMATICAS
a = 10
b = 3

print (a+b) #adição: 13
print (a-b) #subtração: 7
print (a*b) #multiplicação: 30
print (a/b) #divisão: 3.333333

#Divisão inteira e modulo
print(a//b) # divisão inteira : 3
print(a%b) #modulo: 1 - resto da divisão

#POTENCIAÇÃO E RAIZ QUADRADA
print(a ** 2) #potenciação: 100
print(math.sqrt(a)) #raiz quadrada: 3.1622776601682795

#PRECEDENCIA DE OPERADORES
print(2 + 3 * 4) #14
print((2+3)*4) #20

#OPERAÇÕES COM STRINGS
str1 = "Hello"
str2 = "Word"
print(str1 + " "+ str2) # hello word

#REPETIÇÃO
print("Ha" * 3) #HaHaHa

#INDEXAÇÃO E FATIAMENTO BASICOS
s = "Python"
print(s[0]) #P
print(s[1:4]) # yth
print(s[::-1]) # nohtyP (inverte a string)

#IGUALDADE, DESIGUALDADE
print( 5 == 5) #true
print(5 != 6) #true

#MAIOR QUE, MENOR QUE, MAIOR OU IGUAL, MENOR OU IGUAL

print(5 > 3) # True
print(5 < 3) # False
print(5 >= 5) # True
print(5 <= 4) # False

#COMPARAÇÕES COM DIFERENTES TIPOS DE DADOS

print(5 == 5.0) # True
print("5" == 5) # False
print(True == 1) # True
print(False == 0) # True

#OPERAÇÕES LOGICAS

print(True and False)  # False
print(True or False)  # True
print(not True) # False

#USO COM BOOLEANOS E OUTROS TIPOS DE DADOS
print(5 and 3) #3
print(0 or 2) #2
print(not []) #true

#conversão entre tipos de dados
print(int("5")) #5
print(float("3.14")) #3.14
print(str(42)) #"42"
print(bool(1)) #true

#POSSIVEIS ERROS
try:
    print(int("3.14")) # ERRO: NÃO PODE CONVERTER FLOAT STRING PARA INT
except ValueError as e:
    print(f"Erro: {e}")

print(int(3.14)) #3 (trunca o float)
print(bool("")) #false (string vazia e considerada false)
















