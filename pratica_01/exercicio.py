valor_hora = float(input("digite o valor por hora:"))
horas = float(input("digite a quantidade de horas trabalhadas:"))

valor_bruto = horas * valor_hora
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

print("\n--- resultado ---")
print("valor bruto: R$", valor_bruto)
print("impostos (15%): R$", impostos)
print("valor liquido: R$",valor_liquido)