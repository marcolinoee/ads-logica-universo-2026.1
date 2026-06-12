# 1. Declarar a matriz
notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0]
]

# 2. Exibir a matriz antes da alteração
print("Matriz original:")
for linha in notas:
    print(linha)

# 3. Alterar notas[1][0] para 6.5
notas[1][0] = 6.5

# 4. Alterar notas[2][2] para 9.5
notas[2][2] = 9.5

# 5. Exibir a matriz depois da alteração
print("\nMatriz após alterações:")
for linha in notas:
    print(linha)

# Desafio extra: pedir ao usuário linha, coluna e novo valor
linha = int(input("\nDigite o índice da linha (0 a 2): "))
coluna = int(input("Digite o índice da coluna (0 a 2): "))
novo_valor = float(input("Digite o novo valor: "))

# Atualizar célula informada
notas[linha][coluna] = novo_valor

print("\nMatriz atualizada pelo usuário:")
for linha in notas:
    print(linha)
