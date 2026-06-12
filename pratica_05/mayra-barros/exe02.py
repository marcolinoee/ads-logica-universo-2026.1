matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# 1. Primeira linha e primeira coluna
print("Primeira linha, primeira coluna:", matriz[0][0])

# 2. Segunda linha e terceira coluna
print("Segunda linha, terceira coluna:", matriz[1][2])

# 3. Terceira linha e segunda coluna
print("Terceira linha, segunda coluna:", matriz[2][1])

# 4. Segunda linha completa
print("Segunda linha completa:", matriz[1])

# Pergunta obrigatória:
# matriz[1][2] não representa a primeira linha e segunda coluna
# porque em Python os índices começam em 0.
# Assim, matriz[1] é a SEGUNDA linha, e dentro dela [2] é a TERCEIRA coluna.
