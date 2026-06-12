# Declarar a matriz da sala
sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

# Inicializar contadores
livres = 0
ocupados = 0

# Percorrer a matriz
for linha in sala:
    for assento in linha:
        if assento == "L":
            livres += 1
        elif assento == "O":
            ocupados += 1

# Exibir resultados
print("Assentos livres:", livres)
print("Assentos ocupados:", ocupados)

# Desafio extra: percentual de ocupação
total = livres + ocupados
percentual_ocupacao = (ocupados / total) * 100
print(f"Percentual de ocupação: {percentual_ocupacao:.2f}%")
