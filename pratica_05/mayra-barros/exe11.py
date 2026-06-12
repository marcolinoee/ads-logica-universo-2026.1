# Lista de nomes
nomes = ["Ana", "Bruno", "Carla", "Diego"]

# Matriz de notas
notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

# Calcular médias e situação
for i in range(len(nomes)):
    soma = sum(notas[i])
    media = soma / len(notas[i])

    # Decisão condicional
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"  # desafio extra

    print(f"{nomes[i]} - Média: {media:.2f} - {situacao}")
