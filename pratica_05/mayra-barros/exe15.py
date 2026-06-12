# Declarar a matriz da sala
sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

# Função para exibir a sala em formato de tabela
def mostrar_sala(sala):
    for linha in sala:
        print(" ".join(linha))
    print()

# Exibir sala inicial
print("Situação inicial da sala:")
mostrar_sala(sala)

while True:
    # 1. Pedir linha e coluna
    linha = int(input("Digite a linha desejada (ou -1 para sair): "))
    if linha == -1:
        break
    coluna = int(input("Digite a coluna desejada: "))

    # 3. Verificar limites da matriz
    if linha < 0 or linha >= len(sala) or coluna < 0 or coluna >= len(sala[0]):
        print("Posição inválida.")
    else:
        # 4 e 5. Verificar se assento está livre ou ocupado
        if sala[linha][coluna] == "L":
            sala[linha][coluna] = "O"
            print("Reserva realizada.")
        else:
            print("Assento indisponível.")

    # 6. Exibir sala atualizada
    mostrar_sala(sala)
