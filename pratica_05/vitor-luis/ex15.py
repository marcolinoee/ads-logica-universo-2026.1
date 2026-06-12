# ex15.py
# Grade de assentos: reserva de posição 
linha = 0
coluna = 0

sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"],
]

while True:
    linha = int(input("Digite a linha (-1 para sair): "))

    if linha == -1:
        break

    coluna = int(input("Digite a coluna (-1 para sair): "))

    if coluna == -1:
        break

    if linha < 0 or linha >= len(sala) or coluna < 0 or coluna >= len(sala[0]):
        print("Posição fora do escopo")
        continue

    if sala[linha][coluna] == "L":
        sala[linha][coluna] = "O"
        print("Reserva realizada.")
    else:
        print("Assento indisponível")

for linha in sala:
    print(linha)
