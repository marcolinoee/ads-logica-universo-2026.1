# ex22.py
# Depuração: matriz irregular

# Versão com bug
"""
dados = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

for i in range(len(dados)):
    for j in range(3):
        print(dados[i][j])
"""

# Versão segura
dados = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

for i in range(len(dados)):
    for j in range(len(dados[i])):
        print(dados[i][j])

# por que range(3) não é seguro nesse caso?
##############################
# O range(3) assume que todas as linhas contêm 3 elementos,
# o que não acontece nessa matriz irregular, onde a linha 1
# só tem 2 elementos
