# Teste de mesa + caso de teste

def calcular_total(preco, quantidade):
    # verifica valores invalidos
    if preco < 0 or quantidade < 0:
        return "Valores invalidos"

    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto

    # teste de mesa
    print("Preco:", preco)
    print("Quantidade:", quantidade)
    print("Subtotal:", subtotal)
    print("Desconto:", desconto)
    print("Total:", total)

    return total

# -----------------------------
# TESTE DE MESA
# -----------------------------

print("TESTE DE MESA")
resultado = calcular_total(50, 2)

print("\nResultado final:", resultado)


# -----------------------------
# CASOS DE TESTE
# -----------------------------

print("\nCASOS NORMAIS")

print(calcular_total(20, 3))
print(calcular_total(100, 1))


print("\nCASO LIMITROFE")

print(calcular_total(50, 0))


print("\nCASO EXTREMO")

print(calcular_total(1000000, 5000))