# Declarar a matriz
numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

# Inicializar maior e menor com o primeiro elemento
maior = numeros[0][0]
menor = numeros[0][0]
pos_maior = (0, 0)
pos_menor = (0, 0)

# Percorrer a matriz
for i in range(len(numeros)):
    for j in range(len(numeros[i])):
        valor = numeros[i][j]
        if valor > maior:
            maior = valor
            pos_maior = (i, j)
        if valor < menor:
            menor = valor
            pos_menor = (i, j)

# Exibir resultados
print("Maior valor:", maior)
print("Menor valor:", menor)

# Desafio extra: mostrar posições
print(f"Posição do maior valor: linha {pos_maior[0]}, coluna {pos_maior[1]}")
print(f"Posição do menor valor: linha {pos_menor[0]}, coluna {pos_menor[1]}")
