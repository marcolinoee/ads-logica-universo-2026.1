# ex08.py
# Maior e menor valor da matriz

numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

maior_valor = 0
menor_valor = numeros[1][1]

linha_maior = 0
coluna_maior = 0

linha_menor = 0
coluna_menor = 0

for linha in range(len(numeros)):
    for coluna in range(len(numeros[linha])):
        valor = numeros[linha][coluna]

        if valor > maior_valor:
            maior_valor = valor
            linha_maior = linha
            coluna_maior = coluna

        elif valor < menor_valor:
            menor_valor = valor
            linha_menor = linha
            coluna_menor = coluna
        

print(f"Maior valor: {maior_valor}")
print(f"Posição: [{linha_maior}][{coluna_maior}]")

print(f"Menor valor: {menor_valor}")
print(f"Posição: [{linha_menor}][{coluna_menor}]")
