print("1. Somar ")
print("2. Subtrair ")
print("0. Sair ")

menu = int(input("Escolha uma opção: "))

while True:
    if menu == 1:
        somar1 = int(input("Qual o primeiro número? "))
        somar2 = int(input("Qual o segundo número? "))
        resultado_somar = somar1 + somar2
        print(f"O resultado é: {resultado_somar}. ")
        print("1. Somar ")
        print("2. Subtrair ")
        print("0. Sair ")
        menu = int(input("Escolha uma opção: "))
        
    elif menu == 2 :
        subtrair1 = int(input("Digite o primeiro número: "))
        subtrair2 = int(input("Digite o segundo número: "))
        resultado_subtrair = subtrair1 - subtrair2
        print(f"O resultado sa subtração é: {resultado_subtrair}. ")
        print("1. Somar ")
        print("2. Subtrair ")
        print("0. Sair ")
        menu = int(input("Escolha uma opção: "))
        
    elif menu == 0:
        print("Você escolheu sair. ")
        break
    else:
        print("1. Somar ")
        print("2. Subtrair ")
        print("0. Sair ")
        menu = int(input("Escolha uma opção: "))