presentes_bruto = [" maria ", "JOÃO", "ana clara", "Bruno ", " carla"]
consulta = "joão"

# 1. Criar nova lista com nomes padronizados
presentes = []
for nome in presentes_bruto:
    presentes.append(nome.strip().title())

# 2. Padronizar também o nome da consulta
consulta_padronizada = consulta.strip().title()

# 3. Verificar se o estudante consultado está na lista
if consulta_padronizada in presentes:
    mensagem = f"{consulta_padronizada} está presente na lista."
else:
    mensagem = f"{consulta_padronizada} não está presente na lista."

# 4. Exibir resultados
print("Lista final de presentes:", presentes)
print(mensagem)
