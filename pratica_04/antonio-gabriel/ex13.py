# Erros comuns e correção

# a) Problema com o método sort()

# o método sort() organiza a lista,
# mas não retorna uma nova lista
# por isso o resultado vira None
lista = [3, 1, 2]
lista.sort()
print(lista)


# b) Problema com índice que não existe

# o erro acontece porque a lista
# so possui indices 0 e 1
# o indice 5 nao existe
nomes = ["Ana", "Bruno"]

if len(nomes) > 5:
    print(nomes[5])
else:
    print("Indice não existe")

# Desafio opcional



# erro:
# strings nao podem ser alteradas diretamente
# palavra[0] = "J"

# Forma correta do código
palavra = "Python"
palavra = "J" + palavra[1:]
print(palavra)