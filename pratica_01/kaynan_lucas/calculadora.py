def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b

def mostrar_menu():
    print("Calculadora Simples")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

while True:
    mostrar_menu()
    escolha = input("Escolha uma operação (1-5): ")

    if escolha == '5':
        print("Saindo da calculadora. Até mais!")
        break

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = somar(num1, num2)
            print(f"Resultado: {resultado}")
        elif escolha == '2':
            resultado = subtrair(num1, num2)
            print(f"Resultado: {resultado}")
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
            print(f"Resultado: {resultado}")
        elif escolha == '4':
            resultado = dividir(num1, num2)
            print(f"Resultado: {resultado}")
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")
    except ValueError:
        print("Entrada inválida. Por favor, apenas números são permitidos.")
    