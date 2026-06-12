nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]

nomes_padronizados = []

for nome in nomes_brutos:
    nome_limpo = nome.strip().title()
    nomes_padronizados.append(nome_limpo)

print("Lista final:", nomes_padronizados)
print("Quantidade de nomes:", len(nomes_padronizados))