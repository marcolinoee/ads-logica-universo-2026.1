#calculo de troco

#inserir o valor total da compra
total_compra = float(input("Digite o valor total da compra: "))

#inserir o valor pago pelo cliente
valor_pago = float(input("Digite o valor pago pelo cliente: "))

#calcular o troco
troco = valor_pago - total_compra

#exibir o troco
print(f"O troco é: {troco:.2f}")