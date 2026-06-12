# Declarar a matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Percorrer por índice
for i in range(len(matriz)):          # percorre linhas
    for j in range(len(matriz[i])):   # percorre colunas
        print(f"Linha {i} Coluna {j} Valor {matriz[i][j]}")


# O percurso por índice é mais útil quando precisamos saber a posição exata
# de cada elemento, seja para alterar valores, acessar células específicas
# ou trabalhar com estruturas que dependem dos índices (como matrizes grandes,
# tabelas ou quando precisamos cruzar dados).
