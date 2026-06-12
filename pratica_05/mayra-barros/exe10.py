# Lista de nomes
nomes = ["Ana", "Bruno", "Carla", "Diego"]

# Matriz de notas
notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

# Calcular e exibir médias
for i in range(len(nomes)):
    soma = sum(notas[i])              # soma das notas do estudante
    media = soma / len(notas[i])      # média = soma / quantidade de notas
    print(f"{nomes[i]} - Média: {media:.2f}")  # formatado com 2 casas decimais
