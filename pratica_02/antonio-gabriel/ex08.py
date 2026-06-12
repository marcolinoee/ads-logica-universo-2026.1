numero = int(input("Qual a tabuada que você deseja? "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")