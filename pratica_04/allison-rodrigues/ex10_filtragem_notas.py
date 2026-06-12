notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]

# 1. Criar lista de aprovados
aprovados = []

# 2. Percorrer a lista de notas
for nota in notas:
    # 3. Adicionar somente as notas aprovadas
    if nota >= 7.0:
        aprovados.append(nota)

# 4. Exibir a lista final
print("Notas aprovadas:", aprovados)

# Desafio opcional: quantidade de aprovados
print("Quantidade de estudantes aprovados:", len(aprovados))
