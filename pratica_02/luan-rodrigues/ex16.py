# variável para armazenar a resposta
resposta = ""

# contador de respostas S
contador_s = 0

# repete até o usuário digitar FIM
while resposta != "FIM":

    # lê a resposta
    resposta = input("Digite S, N ou FIM: ")

    # verifica se a resposta foi S
    if resposta == "S":
        contador_s += 1

# mostra a quantidade de respostas S
print(f"Quantidade de respostas S: {contador_s}")