# Critérios adotados:
# - Até R$ 100.00: Sem desconto
# - De R$ 100.01 até R$ 500.00: Desconto básico
# - Acima de R$ 500.00: Desconto especial

continuar = "S"

while continuar == "S" or continuar == "s":
    valor = float(input("Digite o valor da compra: "))
    
    if valor <= 100:
        print("Classificação: Sem desconto")
    elif valor <= 500:
        print("Classificação: Desconto básico")
    else:
        print("Classificação: Desconto especial")
        
    continuar = input("Deseja continuar inserindo compras? (S/N): ")