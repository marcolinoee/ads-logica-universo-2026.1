# Declarar a matriz
valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

# Usar acumulador para somar todos os elementos
soma_total = 0
for linha in valores:
    for elemento in linha:
        soma_total += elemento

print("Soma total:", soma_total)

# Desafio extra: calcular a média geral
quantidade_elementos = len(valores) * len(valores[0])
media = soma_total / quantidade_elementos
print("Média geral:", media)
