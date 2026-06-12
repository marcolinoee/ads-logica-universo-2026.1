# Separando e reunindo texto

nome_completo = "Maria Clara Souza"

# separando o nome
nomes = nome_completo.split()

# mostrando a lista
print(nomes)

# juntando com hifen
novo_nome = "-".join(nomes)

# mostrando o resultado
print("Nome com hífen: ",(novo_nome))

print(f"Primeiro nome: {nome_completo.split()[0]}")
print(f"Último nome: {nome_completo.split()[2]}")