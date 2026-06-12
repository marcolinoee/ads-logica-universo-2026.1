# Critérios dos descontos
# Até R$100 o cliente não tem desconto
# De R$100,01 até R$500 o desconto vai ser básico
# Acima de R$500 o desconto do cliente vai ser um desconto especial

while True:
    valor = float(input("Digite o valor da compra: R$ "))

    if valor <= 100:
        print("Classificação: Sem desconto")

    elif valor <= 500:
        print("Classificação: Desconto básico")

    else:
        print("Classificação: Desconto especial")

    continuar = input("Deseja continuar? (s/n): ")

    if continuar == "n":
        print("Programa encerrado.")
        break

    elif continuar == "s":
        continuar = input("Deseja continuar? (s/n): ")
        
    else:
        print("Não foi possível identificar sua reposta, tente outra vez. ")
        continuar = input("Deseja continuar? (s/n): ")