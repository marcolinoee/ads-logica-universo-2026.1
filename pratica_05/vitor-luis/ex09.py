# ex09.py
# Maior valor e sua posição

numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

maior_valor = numeros[0][0]
linha_maior = 0
coluna_maior = 0

for linha in range(len(numeros)):
    for coluna in range(len(numeros[linha])):
        valor = numeros[linha][coluna]

        if valor > maior_valor:
            maior_valor = valor
            linha_maior = linha
            coluna_maior = coluna

print(f"Maior valor: {maior_valor}")
print(f"Linha: {linha_maior}")
print(f"Coluna: {coluna_maior}")

# Por que foi necessário usar índices neste exercício?
########################
# Foi necessário usar índices porque precisávamos descobrir a posição exata do valor dentro da matriz
