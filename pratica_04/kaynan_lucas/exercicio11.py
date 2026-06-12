presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão"

presentes = []

for nome in presentes_bruto:
    presentes.append(nome.strip().title())

consulta = consulta.strip().title()

print("Lista final:", presentes)

if consulta in presentes:
    print("Aluno presente.")
else:
    print("Aluno ausente.")