# Inicialização incorreta
matriz = [[0] * 3] * 3
matriz[0][0] = 1
print(matriz)

# Resultado inesperado:
# [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# Explicação:
# O problema ocorre porque a expressão [[0] * 3] * 3 cria três referências
# para a MESMA lista interna. Assim, ao alterar matriz[0][0],
# todas as linhas são afetadas simultaneamente.

# Versão corrigida usando compreensão de listas
matriz = [[0 for coluna in range(3)] for linha in range(3)]
matriz[0][0] = 1
print(matriz)

# Resultado esperado:
# [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
