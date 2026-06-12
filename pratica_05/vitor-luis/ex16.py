# ex16.py
# Controle de presença em matriz

qtd_faltas = 0
qtd_presentes = 0

presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

for linha in presencas:
    for valor in linha:
        if valor == "P":
            qtd_presentes += 1
        elif valor == "F":
            qtd_faltas += 1

total_registros = qtd_faltas + qtd_presentes
percentual_presenca = (qtd_presentes / total_registros) * 100

print(f"Total de presenças: {qtd_presentes}")
print(f"Total de faltas: {qtd_faltas}")
print(f"Percentual de presença: {percentual_presenca}")

