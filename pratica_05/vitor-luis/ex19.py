# ex19.py
# Tabuleiro de jogo da velha

def exibir_tabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        print(" | ".join(tabuleiro[i]))

        if i < len(tabuleiro) - 1:
            print("-" * 9)


tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

exibir_tabuleiro(tabuleiro)
