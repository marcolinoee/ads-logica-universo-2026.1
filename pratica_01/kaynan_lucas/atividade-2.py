valor_hora = float(input("Digite o valor por hora: "))
horas = float(input("Digite a quantidade de horas: "))

valor_bruto = valor_hora * horas
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

print(f"Valor bruto: R$ {valor_bruto}")
print(f"Impostos (15%): R$ {impostos}")
print(f"Valor líquido: R$ {valor_liquido}")
