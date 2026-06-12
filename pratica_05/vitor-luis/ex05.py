# ex05.py
# Percorrendo uma matriz por índice

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(
            f"Linha: {linha} "
            f"Coluna: {coluna} "    
            f"Valor: {matriz[linha][coluna]} "
        )

# em que situações o percurso por índice é mais útil que o percurso por valor?
########################
# O percurso por índice é mais útil quando precisamos saber a posição do elemento,
# alterar valores da matriz ou acessar elementos vizinhos
