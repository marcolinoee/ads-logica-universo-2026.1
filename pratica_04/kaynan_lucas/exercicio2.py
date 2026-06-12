nome_completo = "Maria Clara Souza"

partes = nome_completo.split()

print("Lista:", partes)

nome_hifen = "-".join(partes)

print("Com hífen:", nome_hifen)

print("Primeiro nome:", partes[0])
print("Último sobrenome:", partes[-1])