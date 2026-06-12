# Declarar a matriz (mesma do exercício 8)
numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

# Inicializar maior valor e posição
maior = numeros[0][0]
linha_maior = 0
coluna_maior = 0

# Percorrer a matriz com índices
for i in range(len(numeros)):
    for j in range(len(numeros[i])):
        if numeros[i][j] > maior:
            maior = numeros[i][j]
            linha_maior = i
            coluna_maior = j

# Exibir resultados
print("Maior valor:", maior)
print("Linha:", linha_maior)
print("Coluna:", coluna_maior)

# Pergunta obrigatória:
# Foi necessário usar índices porque não basta saber o valor máximo,
# precisamos também identificar sua posição exata (linha e coluna).
# Sem índices, só teríamos o valor, mas não conseguiríamos localizar onde ele está na matriz.
