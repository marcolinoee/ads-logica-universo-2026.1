tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

linha = int(input("Linha (0 a 2): "))
coluna = int(input("Coluna (0 a 2): "))
simbolo = input("Símbolo (X ou O): ").upper()

if simbolo != "X" and simbolo != "O":
    print("Símbolo inválido.")
else:
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = simbolo
        print("Jogada realizada!")
    else:
        print("Jogada inválida.")

for i in range(len(tabuleiro)):
    print(" | ".join(tabuleiro[i]))

    if i < len(tabuleiro) - 1:
        print("-" * 9)
