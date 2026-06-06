soma = 0

for i in range(8):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        soma = soma + num

print("Soma dos pares:", soma)