# a)
lista = [3, 1, 2]

lista.sort()

print(lista)

# O erro acontece porque sort() altera a lista e retorna None.


# b)
nomes = ["Ana", "Bruno"]

if len(nomes) > 5:
    print(nomes[5])
else:
    print("Índice não existe.")

# O erro acontecia porque tentava acessar uma posição inexistente.