continuar = "S"

while continuar == "S":
    valor = float(input("Digite o valor da compra: "))
    print("Compra registrada: R$", valor)
    continuar = input("Deseja continuar? (S/N): ")

print("Programa encerrado")