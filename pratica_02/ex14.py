# O PROBLEMA: O código entrava em loop infinito porque a variável de controle diminuía (i = i - 1), 
# mas a condição testava se ela era maior que zero (while i > 0). Como começava em 10 e só diminuía, 
# ela sempre seria menor ou igual a 10, mas o erro comum é somar por engano (i = i + 1) no loop, 
# fazendo com que o número cresça para sempre e nunca chegue a 0, ou esquecer de atualizar a variável.

i = 10

while i >= 1:
    print(i)
    i = i - 1  # Correção: garante que o número diminua até chegar a 0 e encerrar o laço