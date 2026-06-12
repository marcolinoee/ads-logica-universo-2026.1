# Tabuleiro inicial (mesmo do exercício 19)
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

# Exibir tabuleiro inicial
print("Tabuleiro inicial:")
exibir_tabuleiro(tabuleiro)

# 1. Pedir linha e coluna
linha = int(input("Digite a linha (0 a 2): "))
coluna = int(input("Digite a coluna (0 a 2): "))

# 2. Pedir símbolo
simbolo = input("Digite o símbolo (X ou O): ").upper()

# Desafio extra: validar símbolo
if simbolo not in ["X", "O"]:
    print("Símbolo inválido. Use apenas X ou O.")
else:
    # 3. Verificar se posição está vazia
    if tabuleiro[linha][coluna] == " ":
        # 4. Realizar jogada
        tabuleiro[linha][coluna] = simbolo
        print("Jogada realizada.")
    else:
        # 5. Jogada inválida
        print("Jogada inválida. Posição já ocupada.")

# 6. Exibir tabuleiro atualizado
print("\nTabuleiro atualizado:")
exibir_tabuleiro(tabuleiro)
