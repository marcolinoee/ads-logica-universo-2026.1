# Projeto integrador curto


# ETAPA 1 - Dados Iniciais

nomes_brutos = ["  ana ", "BRUNO", "carla  ", "Daniel"]
notas = [7.5, 5.0, 8.0, 6.5]
consulta = "bruno"

# ETAPA 2 - Padronização de nomes

nomes = []

for nome in nomes_brutos:
    nome = nome.strip()
    nome = nome.lower()
    nomes.append(nome)

# ETAPA 3 - Filtrando aprovados

aprovados = []

for nota in notas:
    if nota >= 7:
        aprovados.append(nota)

# ETAPA 4 - Buscar por estudante

consulta = consulta.strip()
consulta = consulta.lower()

encontrado = False

for nome in nomes:
    if nome == consulta:
        encontrado = True
        break

# ETAPA 5 - Relatório final

print("Relatório Final")

print(f"\nLista de estudantes: {nomes}")
print(f"\nNotas aprovadas: {aprovados}")
print(f"\nTotal de estudantes: {len(nomes)}")
print(f"Total de aprovados: {len(aprovados)}")

if encontrado:
    print(f"\nO estudante {consulta} esta presente")
else:
    print(f"\nO estudante {consulta} nao esta presente")