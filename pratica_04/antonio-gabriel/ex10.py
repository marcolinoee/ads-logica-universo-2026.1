# Filtragem de notas

notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]

aprovados = []

for nota in notas:
    if nota >= 7:
        aprovados.append(nota)

print(f"As notas aprovadas foram: {aprovados}")
print(f"As quantidade notas aprovadas são: {len(aprovados)}")