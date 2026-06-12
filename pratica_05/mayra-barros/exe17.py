# Matriz de presença (mesma do exercício 16)
presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

# Percorrer cada estudante (linha)
for i in range(len(presencas)):
    faltas = presencas[i].count("F")  # conta quantos "F" existem na linha
    # Desafio extra: situação
    if faltas <= 1:
        situacao = "Frequência adequada"
    else:
        situacao = "Atenção à frequência"
    print(f"Estudante {i} - Faltas: {faltas} - {situacao}")
