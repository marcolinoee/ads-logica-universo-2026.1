# ex13.py
# Média por avaliação

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

for coluna in range(len(notas[0])):
    soma = 0
    
    for linha in range(len(notas)):
        soma += notas[linha][coluna]

    media = soma / len(notas)

    print(f"Avaliação {coluna} - Média: {media:.2f}")

# por que neste exercício o laço externo pode percorrer as colunas?
################################
# O laço externo percorre as colunas porque cada coluna representa uma
# avaliação, já o laço interno percorre as linhas para acessar as notas
# de todos os alunos daquela avaliação e calcular sua média
