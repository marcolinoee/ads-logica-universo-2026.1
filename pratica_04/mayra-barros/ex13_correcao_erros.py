# (a) Problema:
# lista.sort() organiza a lista, mas não retorna nada (retorna None).
# Por isso, 'resultado' recebe None e o print mostra None.

lista = [3, 1, 2]
lista.sort()  # ordena a lista diretamente
print(lista)  # saída correta: [1, 2, 3]

# Alternativa: usar sorted(), que retorna uma nova lista ordenada
lista = [3, 1, 2]
resultado = sorted(lista)
print(resultado)  # saída correta: [1, 2, 3]


# (b) Problema:
# nomes[5] tenta acessar a posição 5, mas a lista só tem 2 elementos (índices 0 e 1).
# Isso gera erro IndexError.

nomes = ["Ana", "Bruno"]

# Forma segura: verificar o tamanho da lista antes de acessar
indice = 1
if indice < len(nomes):
    print(nomes[indice])
else:
    print("Índice fora do alcance da lista.")


# (c) Desafio opcional: criar outro erro e corrigir
# Exemplo: tentar acessar caractere inexistente em string
palavra = "Python"
try:
    print(palavra[10])  # erro: índice fora do alcance
except IndexError:
    print("Índice inválido na string.")
