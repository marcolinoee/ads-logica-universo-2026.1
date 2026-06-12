valor_hora = float(input("Digite o valor por hora: "))
horas = float(input("Digite a quantidade de horas: "))

valor_bruto = horas * valor_hora
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

print("\n --- RESULTADO ---")
print(f"Valor bruto: R$ {valor_bruto:.2f}")
print(f"Impostos (15%):  R$ {valor_bruto:.2f}")
print(f"Valor líquido: R$ {valor_liquido:.2f}")