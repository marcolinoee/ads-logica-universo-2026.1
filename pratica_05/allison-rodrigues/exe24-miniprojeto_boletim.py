# Lista de nomes dos estudantes
nomes = ["Ana", "Bruno", "Carla", "Diego", "Eduardo"]

# Matriz de notas (4 notas para cada estudante)
notas = [
    [8.0, 7.5, 9.0, 8.5],
    [5.0, 6.0, 5.5, 6.5],
    [9.0, 8.5, 10.0, 9.5],
    [6.5, 7.0, 6.0, 6.5],
    [4.0, 5.0, 4.5, 5.0]
]

# Inicializar maior e menor média
maior_media = 0
menor_media = 10
nome_maior = ""
nome_menor = ""

print("=== Relatório Final ===")

# Calcular médias e situação
for i in range(len(nomes)):
    soma = sum(notas[i])
    media = soma / len(notas[i])

    # Classificação
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    # Atualizar maior e menor média
    if media > maior_media:
        maior_media = media
        nome_maior = nomes[i]
    if media < menor_media:
        menor_media = media
        nome_menor = nomes[i]

    # Exibir relatório individual
    print(f"{nomes[i]} - Média: {media:.2f} - {situacao}")

# Exibir maior e menor média da turma
print("\nMaior média da turma:", f"{nome_maior} - {maior_media:.2f}")
print("Menor média da turma:", f"{nome_menor} - {menor_media:.2f}")
