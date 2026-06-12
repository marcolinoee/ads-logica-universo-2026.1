notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]

aprovadas = []

for nota in notas:
    if nota >= 7.0:
        aprovadas.append(nota)

print("Notas aprovadas:", aprovadas)
print("Quantidade de aprovados:", len(aprovadas))