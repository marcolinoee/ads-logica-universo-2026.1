# Limpeza e padronização de nomes

nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]

nomes_padronizados = []

for nome in nomes_brutos:
    nome = nome.strip()
    nome = nome.title()
    nomes_padronizados.append(nome)

print(f"Nomes: {nomes_padronizados}")
print(f"Quantidade de nomes: {len(nomes_padronizados)}")