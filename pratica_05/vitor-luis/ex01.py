# ex01.py
# Criando e exibindo uma matriz 3x3

matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for linha in matriz:
    for valor in linha:
        print(valor, end=" ")
    print()

print(f"Linhas: {len(matriz)}")
print(f"Colunas: {len(matriz[0])}")
