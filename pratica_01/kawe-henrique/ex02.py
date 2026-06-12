# Entrada de dados
valor_hora = float(input("Digite o valor cobrado por hora: R$ "))
horas_estimadas = float(input("Digite a estimativa de horas para o projeto: "))

# Cálculos
valor_bruto = valor_hora * horas_estimadas
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

# Exibição dos resultados
print("-" * 35)
print(f"RESUMO DO ORÇAMENTO")
print("-" * 35)
print(f"Valor Bruto:     R$ {valor_bruto:8.2f}")
# A linha abaixo foi corrigida:
print(f"Impostos (15%):  R$ {impostos:8.2f}")
print(f"Valor Líquido:   R$ {valor_liquido:8.2f}")
print("-" * 35)