positivos = 0

for i in range(10):
    num = float(input("Digite um número: "))
    if num > 0:
        positivos = positivos + 1

print("Quantidade de positivos:", positivos)