# Busca linear de um elemento

estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"

encontrado = False

for estudante in estudantes:
    if estudante == procurado:
        encontrado = True
        break

if encontrado:
    print("Nome encontrado")
else:
    print("Nome nao encontrado")