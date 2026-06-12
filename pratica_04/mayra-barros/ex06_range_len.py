alunos = ["Ana", "Bruno", "Carla", "Daniel"]

# 1. Usando for com range(len(alunos))
for i in range(len(alunos)):
    print(f"Posição {i} -> {alunos[i]}")

# Desafio opcional:
# Mostrar no formato Índice 0 -> Ana
print("\nFormato desafio:")
for i in range(len(alunos)):
    print(f"Índice {i} -> {alunos[i]}")
