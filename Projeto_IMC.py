#PROJETO MÊS 1
#CALCULADORA DE IMC
peso = float(input("Digite o seu peso em kg:"))
altura = float(input("Digite a sua altura em metros:"))
imc = peso / (altura**2)
print(f"O seu IMC é:{imc:.2f}")
if (imc < 18.5):
    print(f"Abaixo do peso.")
elif (18.5 <= imc < 25 ):
    print(f"Peso normal")
elif(25 <= imc < 30):
    print(f"Sobrepeso")
else:
    print(f"Obeso")

#---------------------------------------------------------------------------
#PROJETO MÊS 1
#CONVERSOR DE MEDIDAS
escolha = (input("Escolha a medida:\n C - Celsius \n F - Fahrenheit \n K - Kelvin:")).upper()
temp = float(input("Digite a temperatura:"))
convertida = (input("Escolha a medida para conversão:\n C - Celsius \n F - Fahrenheit \n K - Kelvin:")).upper()

if (escolha == "C" and convertida == "F"):
    Fahrenheit = (temp*(9/5))+32
    print(f"A conversão da temperatura {temp}°C em Celsius equivale a {Fahrenheit}°F")
elif (escolha == "C" and convertida == "K"):
    Kelvin = (temp+273.15)
    print(f"A conversão da temperatura {temp}°C em Celsius equivale a {Kelvin}°K")
elif (escolha == "F" and convertida == "C"):
    Celsius = (temp-32)*(5/9)
    print(f"A conversão da temperatura {temp}°F em Fahrenheit equivale a {Celsius}°C")
elif (escolha == "F" and convertida == "K"):
    Kelvin = (temp-32)*(5/9)+273.15
    print(f"A conversão da temperatura {temp}°F em Fahrenheit equivale a {Kelvin}°K")
elif (escolha == "K" and convertida == "C"):
    Celsius = (temp-273.15)
    print(f"A conversão da temperatura {temp}°K em Kelvin equivale a {Celsius}°C")
elif (escolha == "K" and convertida == "F"):
    Fahrenheit = (temp-273.15)*(9/5)+32
    print(f"A conversão da temperatura {temp}°K em Kelvin equivale a {Celsius}°F")

#-----------------------------------------------------------------------------------
#PROJETO MÊS 1
#CALCULADORA DE JUROS SIMPLES

cp = float(input("Digite o valor principal - Capital Inicial:"))
taxa_anual = float(input("Digite o percentual da taxa anual (%):"))
tempo = int(input("Digite o tempo em anos do empréstimo:"))

taxa_decimal = taxa_anual/100
js = cp*taxa_decimal*tempo
m = cp + js

print(f"Resultado:")
print(f"Montante final: R${m:.2f}")
print(f"Total de juros: R${js:.2f}")

#-----------------------------------------------------------------------------------
# PROJETO MÊS 1
# CALCULADORA DE GORJETA
total_conta = float(input("Digite o valor total da conta:"))
avaliacao_servico = float(input("Digite o valor do serviço:\n1 - Excelente: 20% de gorjeta \n2 - Bom: 15% de gorjeta \n3 - Regular: 10% de gorjeta \n4 - Ruim: 5% de gorjeta:\n "))

if (avaliacao_servico == 1):
    percentual_gorjeta = 20 / 100
elif (avaliacao_servico == 2):
    percentual_gorjeta = 15 / 100
elif (avaliacao_servico == 3):
    percentual_gorjeta = 10 / 100
elif (avaliacao_servico == 4):
    percentual_gorjeta = 5 / 100

gorjeta = total_conta * percentual_gorjeta
total_apagar = total_conta + gorjeta

print(f"---------NOTINHA-------------")
print(f"Valor da conta: {total_conta:.2f}")
print(f"Percentual da gorjeta:{percentual_gorjeta * 100:.0f}%")
print(f"Valor da gorjeta:{gorjeta:.2f}")
print(f"Valor total a ser pago:{total_apagar:.2f}")




