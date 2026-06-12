def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return subtotal, desconto, total

# Parte A - Teste de mesa
print("Teste de mesa (preço=50, quantidade=2):")
subtotal, desconto, total = calcular_total(50, 2)
print(f"Subtotal: {subtotal}, Desconto: {desconto}, Total: {total}\n")

# Parte B - Casos de teste
print("Casos normais:")
print(calcular_total(30, 3))  # esperado: (90, 9, 81)
print(calcular_total(20, 5))  # esperado: (100, 10, 90)

print("\nCaso limítrofe:")
print(calcular_total(50, 1))  # esperado: (50, 5, 45)

print("\nCaso extremo:")
print(calcular_total(50, 0))  # esperado: (0, 0, 0)
