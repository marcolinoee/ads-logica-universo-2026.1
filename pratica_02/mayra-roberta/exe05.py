contador_positivos = 0

for i in range(10):
    numero = int(input("Digite um número: "))
    if numero > 0:
        contador_positivos = contador_positivos + 1

print("Total de positivos:", contador_positivos)