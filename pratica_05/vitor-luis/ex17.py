# ex17.py
# Faltas por estudante

qtd_falta = 0

presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

for i in range(len(presencas)):
    qtd_falta = 0
    for presenca in presencas[i]:
        if presenca == "F":
            qtd_falta += 1

    if qtd_falta <= 1:
        situacao = "Frequência adequada"
    else:
        situacao = "Atenção à frequência"

    print(f"Estudante {i} - Faltas: {qtd_falta} / {situacao}")
