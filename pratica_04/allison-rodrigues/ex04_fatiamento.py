palavra = "programacao"
valores = [10, 20, 30, 40, 50, 60]

# 1. Exibir os 4 primeiros caracteres da palavra
print("4 primeiros caracteres:", palavra[:4])

# 2. Exibir os caracteres da posição 4 até a 8
print("Caracteres da posição 4 até 8:", palavra[4:9])

# 3. Exibir os três primeiros elementos da lista
print("3 primeiros elementos:", valores[:3])

# 4. Exibir os elementos da posição 2 até o final da lista
print("Elementos da posição 2 até o final:", valores[2:])

# Desafio opcional:
# Testando outros recortes
print("Últimos 3 caracteres da palavra:", palavra[-3:])
print("Valores do meio (posição 1 até 4):", valores[1:5])

# Observação:
# O fatiamento usa índices de início e fim, mas o fim é exclusivo.
# Exemplo: palavra[4:9] pega índices 4,5,6,7,8 (não inclui o 9).
