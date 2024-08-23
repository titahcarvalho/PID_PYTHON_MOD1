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

