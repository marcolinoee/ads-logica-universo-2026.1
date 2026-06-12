# Criar a matriz do tabuleiro
tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        print(" | ".join(tabuleiro[i]))
        if i < len(tabuleiro) - 1:
            print("-" * 9)

# Exibir o tabuleiro
exibir_tabuleiro(tabuleiro)
