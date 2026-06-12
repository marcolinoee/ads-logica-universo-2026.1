# ex21.py
# Depuração: índice fora dos limites

dados = [
    [1, 2],
    [3, 4]
]

print(dados[1][0])

# 1. Qual erro ocorre? -> IndexError: list index out of range
# 2. Por que o erro ocorre? -> A lista dados possui apenas duas linhas, com índices 0 e 1, o código tenta acessar o índice 2, que não existe
# 3. Quais são os índices válidos de linha -> 0 e 1
# 4. Corrija o código pra exibir o valor 3 -> Tá no código
