nomes_brutos = [" ana", "BRUNO ", "CArLa silva", " joão pedro "]

# Lista para armazenar os nomes padronizados
nomes_padronizados = []

for nome in nomes_brutos:
    nome_limpo = nome.strip().title()  # remove espaços e coloca iniciais maiúsculas
    nomes_padronizados.append(nome_limpo)

print("Lista final:", nomes_padronizados)
print("Quantidade de nomes:", len(nomes_padronizados))
