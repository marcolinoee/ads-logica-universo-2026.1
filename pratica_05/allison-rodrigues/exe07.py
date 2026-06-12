# Declarar a matriz (mesma do exercício 6)
valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

# Inicializar contadores
pares = 0
impares = 0
pares_encontrados = []  # desafio extra

# Percorrer a matriz
for linha in valores:
    for elemento in linha:
        if elemento % 2 == 0:
            pares += 1
            pares_encontrados.append(elemento)  # guardar pares
        else:
            impares += 1

# Exibir resultados
print("Pares:", pares)
print("Ímpares:", impares)

# Desafio extra: mostrar lista de pares encontrados
print("Lista de pares encontrados:", pares_encontrados)
