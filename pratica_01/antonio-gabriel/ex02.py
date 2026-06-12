# Entrada de dados
valor_hora = float(input("Digite o valor cobrado por hora: R$ "))
horas = float(input("Digite a quantidade de horas estimadas: "))

# Cálculos
valor_bruto = valor_hora * horas
imposto = valor_bruto * 0.15
valor_liquido = valor_bruto - imposto

# Saída
print("\n===== RESULTADO =====")
print(f"Valor bruto: R$ {valor_bruto:.2f}")
print(f"Imposto (15%): R$ {imposto:.2f}")
print(f"Valor líquido: R$ {valor_liquido:.2f}")