contador_s = 0

resposta = input("Digite S para sim, N para não ou FIM para encerrar: ")

while resposta != "FIM" and "N":
    
    if resposta == "S":
        contador_s = contador_s + 1

    resposta = input("Digite S para sim, N para não ou FIM para encerrar: ")
   
print(f"Quantidade de respostas S: {contador_s} ")