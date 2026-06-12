# Cadastro simples de presença

presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão"

presentes = [] # Lista nova

# Padronização dos nomes
for nome in presentes_bruto:
    nome = nome.strip()
    nome = nome.lower()
    presentes.append(nome)

# Padronizando variavel de consulta
consulta = consulta.strip()
consulta = consulta.lower()

# Verificando se existe
encontrado = False

for nome in presentes:
    if nome == consulta:
        encontrado = True
        break

print(presentes) # Mostrar lista

if encontrado: # Mostrar resultado
    print(f"{consulta} está presente")
else:
    print(f"{consulta} não está presente")