# Criar a matriz do laboratório (4 fileiras x 5 computadores)
laboratorio = [
    ["L", "O", "L", "M", "L"],
    ["L", "L", "O", "L", "M"],
    ["O", "L", "L", "L", "O"],
    ["M", "L", "O", "L", "L"]
]

# Função para exibir o mapa
def exibir_mapa(lab):
    for linha in lab:
        print(" ".join(linha))
    print()

# Função para contar estados
def contar_estados(lab):
    livres = ocupados = manutencao = 0
    for linha in lab:
        for pc in linha:
            if pc == "L":
                livres += 1
            elif pc == "O":
                ocupados += 1
            elif pc == "M":
                manutencao += 1
    return livres, ocupados, manutencao

# Exibir mapa inicial
print("Mapa inicial do laboratório:")
exibir_mapa(laboratorio)

# Contar estados
livres, ocupados, manutencao = contar_estados(laboratorio)
print(f"Livres: {livres}, Ocupados: {ocupados}, Manutenção: {manutencao}\n")

# Permitir reserva
linha = int(input("Digite a linha desejada (0 a 3): "))
coluna = int(input("Digite a coluna desejada (0 a 4): "))

# Verificar limites
if linha < 0 or linha >= len(laboratorio) or coluna < 0 or coluna >= len(laboratorio[0]):
    print("Posição fora dos limites.")
else:
    if laboratorio[linha][coluna] == "L":
        laboratorio[linha][coluna] = "O"
        print("Reserva realizada.")
    elif laboratorio[linha][coluna] == "M":
        print("Computador em manutenção. Não pode ser ocupado.")
    else:
        print("Computador já ocupado.")

# Exibir mapa atualizado
print("\nMapa atualizado do laboratório:")
exibir_mapa(laboratorio)
