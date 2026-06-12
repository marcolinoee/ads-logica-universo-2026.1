# ex07.py
# Contando números pares e ímpares

valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

pares_encontrados = []

pares = 0
impares = 0

for linha in valores:
    for valor in linha:
        if valor % 2 == 0:
            pares += 1
            pares_encontrados.append(valor)
        else:
            impares += 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
print(f"Pares em lista: {pares_encontrados}")
