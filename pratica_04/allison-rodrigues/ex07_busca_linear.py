estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"

# 1. Variável booleana para indicar se foi encontrado
encontrado = False

# 2. Percorrer a lista com for
for aluno in estudantes:
    if aluno == procurado:
        encontrado = True
        break  # 4. Interrompe o laço quando encontrar

# 5. Exibir o resultado final
if encontrado:
    print(f"{procurado} foi encontrado na lista!")
else:
    print(f"{procurado} não está na lista.")
