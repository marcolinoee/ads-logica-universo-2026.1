# Código original com erro
dados = [
    [1, 2],
    [3, 4]
]

# print(dados[2][0])  # ERRO: índice fora dos limites


# 1. Qual erro ocorre?
#    IndexError: list index out of range
#
# 2. Por que o erro ocorre?
#    Porque estamos tentando acessar a linha de índice 2,
#    mas a matriz só possui índices válidos 0 e 1.
#
# 3. Quais são os índices válidos de linha?
#    0 e 1 (já que há apenas duas linhas).
#
# 4. Corrija o código para exibir o valor 3:
print(dados[1][0])  # Correto: exibe 3
