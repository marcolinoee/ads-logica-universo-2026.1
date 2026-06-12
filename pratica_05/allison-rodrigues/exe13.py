# Lista de nomes
nomes = ["Ana", "Bruno", "Carla", "Diego"]

# Matriz de notas
notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

# Percorrer por coluna (avaliações)
for j in range(len(notas[0])):  # número de colunas
    soma = 0
    for i in range(len(notas)):  # número de linhas
        soma += notas[i][j]
    media = soma / len(notas)
    print(f"Avaliação {j} - Média: {media:.2f}")

# Pergunta obrigatória:
# Neste exercício o laço externo percorre as colunas porque queremos calcular
# a média de cada avaliação (cada coluna representa uma avaliação).
# Assim, fixamos a coluna e percorremos todas as linhas para somar as notas
# daquela avaliação.
