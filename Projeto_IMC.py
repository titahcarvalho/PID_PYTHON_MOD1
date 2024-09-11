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