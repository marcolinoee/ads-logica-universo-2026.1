# 1. Declarar a matriz
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# 2. Exibir a matriz linha por linha
for linha in matriz:
    print(linha)

# 3. Mostrar quantidade de linhas e colunas
linhas = len(matriz)
colunas = len(matriz[0])  # assumindo que todas as linhas têm o mesmo tamanho
print("Linhas:", linhas)
print("Colunas:", colunas)

# Desafio extra: exibir como tabela (sem colchetes e vírgulas)
print("\nMatriz em formato de tabela:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()  # quebra de linha
