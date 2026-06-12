#Foi utilizado while porque não sabemos quantas respostas serão digitadas. O laço continua executando até que a condição de parada (FIM) seja informada pelo usuário.




resposta = ""
contador_s = 0

while resposta != "FIM":
    resposta = input("Digite S, N ou FIM: ").upper()

    if resposta == "S":
        contador_s += 1

print("Quantidade de respostas S:", contador_s)