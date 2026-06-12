soma = 0

for i in range(8):
    valor = int(input("Digite um valor inteiro: "))
    if valor % 2 == 0:
        soma = soma + valor

print("Soma dos pares:", soma)