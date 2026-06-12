soma = 0

for i in range(8):

    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        soma = soma + numero

print(f"Soma dos números pares: {soma}. ")