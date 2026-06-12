# Matriz de presença (mesma do exercício 16)
presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

# Inicializar variáveis
maior_faltas = 0
aula_maior = 0

# Percorrer por coluna (cada aula)
for j in range(len(presencas[0])):  # número de colunas
    faltas = 0
    for i in range(len(presencas)):  # número de linhas
        if presencas[i][j] == "F":
            faltas += 1
    # Verificar se esta aula tem mais faltas
    if faltas > maior_faltas:
        maior_faltas = faltas
        aula_maior = j

# Exibir resultado
print("Aula com mais faltas:", aula_maior)
print("Quantidade de faltas:", maior_faltas)
