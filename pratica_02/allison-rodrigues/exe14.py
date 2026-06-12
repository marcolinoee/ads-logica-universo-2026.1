# Versão antiga com while:
# contador_positivos = 0
# i = 0
# while i < 10:
#     numero = int(input("Digite um número: "))
#     if numero > 0:
#         contador_positivos = contador_positivos + 1
#     i = i + 1

# Versão nova com for:
contador_positivos = 0

for i in range(10):
    numero = int(input("Digite um número: "))
    if numero > 0:
        contador_positivos = contador_positivos + 1

print("Total de positivos:", contador_positivos)

# Explicação: Com for ficou mais simples porque não precisei criar
# a variável i nem lembrar de fazer i = i + 1. O for já conta sozinho.