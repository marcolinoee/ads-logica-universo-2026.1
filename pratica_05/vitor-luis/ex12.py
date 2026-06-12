# ex12.py
# Boletim: maior média da turma

maior_media = 0
menor_media = 11
nome_maior = ""
nome_menor = ""

nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

for i in range(len(nomes)):
    soma = 0

    for nota in notas[i]:
        soma += nota
    
    media = soma / len(notas[i])

    if media > maior_media:
        maior_media = media
        nome_maior = nomes[i]
    elif media < menor_media:
        menor_media = media
        nome_menor = nomes[i]

print(f"Maior média: {nome_maior} - {maior_media:.2f}")
print(f"Menor média: {nome_menor} - {menor_media:.2f}")

