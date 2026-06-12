# Lista de nomes
nomes = ["Ana", "Bruno", "Carla", "Diego"]

# Matriz de notas
notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

# Inicializar maior e menor média
maior_media = 0
menor_media = 10
nome_maior = ""
nome_menor = ""

# Calcular médias e identificar extremos
for i in range(len(nomes)):
    soma = sum(notas[i])
    media = soma / len(notas[i])

    if media > maior_media:
        maior_media = media
        nome_maior = nomes[i]

    if media < menor_media:
        menor_media = media
        nome_menor = nomes[i]

# Exibir resultados
print(f"Maior média: {nome_maior} - {maior_media:.2f}")
print(f"Menor média: {nome_menor} - {menor_media:.2f}")
