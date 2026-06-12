# ex14.py
# Grade de assentos: contagem de estados

qtd_ocupados = 0
qtd_livres = 0

sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"],
]

for linha in range(len(sala)):
    for coluna in range(len(sala[linha])):
        if sala[linha][coluna] == "L":
            qtd_livres += 1
        else:
            qtd_ocupados += 1

total_assentos = qtd_livres + qtd_ocupados
porcentagem = (qtd_ocupados / total_assentos) * 100

print(f"Assentos livres: {qtd_livres}")
print(f"Assentos ocupados: {qtd_ocupados}")
print(f"Taxa de ocupação: {porcentagem:.2f}%")
