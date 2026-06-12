# 1. Padronizar nomes de estudantes
estudantes_bruto = [" maria ", "JOÃO", "ana clara", "Bruno ", " carla"]
estudantes = [nome.strip().title() for nome in estudantes_bruto]

# 2. Filtrar notas aprovadas (>= 7.0)
notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]
aprovados = [nota for nota in notas if nota >= 7.0]

# 3. Verificar presença de um nome consultado
consulta = "joão"
consulta_padronizada = consulta.strip().title()
presenca = consulta_padronizada in estudantes

# 4. Exibir relatório final
print("=== Relatório Final ===")
print("Lista de estudantes padronizada:", estudantes)
print("Notas aprovadas:", aprovados)
print("Quantidade de aprovados:", len(aprovados))

if presenca:
    print(f"{consulta_padronizada} está presente na lista.")
else:
    print(f"{consulta_padronizada} não está presente na lista.")
