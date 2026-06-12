# Declarar a matriz de presenças
presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

# Inicializar contadores
total_presencas = 0
total_faltas = 0

# Percorrer a matriz
for linha in presencas:
    for valor in linha:
        if valor == "P":
            total_presencas += 1
        elif valor == "F":
            total_faltas += 1

# Exibir resultados
print("Total de presenças:", total_presencas)
print("Total de faltas:", total_faltas)

# Desafio extra: percentual de presença
total = total_presencas + total_faltas
percentual_presenca = (total_presencas / total) * 100
print(f"Percentual de presença: {percentual_presenca:.2f}%")
