# ex24.py
# Mini-projeto: sistema simples de boletim

nomes = []
notas = []
medias = []

for i in range(5):
    nome = input(f"Digite o nome do estudante: {i + 1}: ")
    nomes.append(nome)

    notas_estudante = []

    print(f"Digite as 4 notas do {nome}: ")
    for j in range(4):
        nota = float(input(f"Nota: {j + 1}: "))
        notas_estudante.append(nota)

    notas.append(notas_estudante)

for estudante in notas:
    media = sum(estudante) / len(estudante)
    medias.append(media)

print("\n" + "=" * 40)
print("RELATÓRIO FINAL")
print("=" * 40)

for i in range(5):
    if medias[i] >= 7.0:
        situacao = "Aprovado"
    elif medias[i] >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f"Nome: {nomes[i]}")
    print(f"Média: {medias[i]:.2f}")
    print(f"Situação: {situacao}")
    print("-" * 40)

maior_media = max(medias)
menor_media = min(medias)

print(f"Maior média da turma: {maior_media:.2f}")
print(f"Menor média da turma: {menor_media:.2f}")
