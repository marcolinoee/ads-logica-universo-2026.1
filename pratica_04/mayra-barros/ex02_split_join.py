nome_completo = "Maria Clara Souza"

# 1. Separar o texto em partes
partes = nome_completo.split()

# 2. Exibir a lista resultante
print("Lista de partes:", partes)

# 3. Reunir com hífen
nome_hifen = "-".join(partes)

# 4. Exibir o texto final
print("Nome com hífen:", nome_hifen)

# Desafio opcional: primeiro nome e último sobrenome
primeiro_nome = partes[0]
ultimo_sobrenome = partes[-1]
print("Primeiro nome:", primeiro_nome)
print("Último sobrenome:", ultimo_sobrenome)
