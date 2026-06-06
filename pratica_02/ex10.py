opcao = -1

while opcao != 0:
    print("\n1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado da soma:", n1 + n2)
    elif opcao == 2:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado da subtração:", n1 - n2)
    elif opcao == 0:
        print("Programa encerrado.")
    else:
        print("Opção inválida!")