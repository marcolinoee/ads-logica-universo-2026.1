votos_sim = 0
resposta = ""

while resposta != "FIM":
    resposta = input("Digite S, N ou FIM: ")
    if resposta == "S" or resposta == "s":
        votos_sim = votos_sim + 1

print("Quantidade de SIM:", votos_sim)

# O 'while' foi usado porque o término depende de uma condição (digitar "FIM"), 
# sem quantidade de repetições definida.