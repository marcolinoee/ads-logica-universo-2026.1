# ex23.py
# Depuração: inicialização incorreta

matriz = [[0] * 3] * 3
matriz[0][0] = 1
print(matriz)

# Resultado: [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# O que aconteceu?
# As três linhas não são listas independentes, o operador * replicou 
# referências para a mesma lista interna, assim, ao alterar matriz[0][0], 
# a alteração apareceu em todas as linhas

# Criação correta da matriz
matriz = [[0 for coluna in range(3)] for linha in range(3)]
matriz[0][0] = 1
print(matriz)

# Resultado:
# [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
