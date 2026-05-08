opcao = -1

while opcao != 0:

    print("\nMENU")
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        soma = num1 + num2

        print(f"Resultado da soma: {soma}")

    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        subtracao = num1 - num2

        print(f"Resultado da subtração: {subtracao}")

    elif opcao == 0:
        print("Programa encerrado.")

    else:
        print("Opção inválida!")