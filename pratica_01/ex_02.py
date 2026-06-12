# Solicitando os dados ao usuário
valor_hora = float(input("Digite o valor cobrado por hora (R$): "))
horas_estimadas = float(input("Digite a estimativa de horas para conclusão: "))

# Cálculos baseados nas fórmulas fornecidas
valor_bruto = horas_estimadas * valor_hora
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

# Exibindo os resultados formatados
print("-" * 30)
print(f"RESUMO DO PROJETO")
print("-" * 30)
print(f"Valor Bruto:    R$ {valor_bruto:,.2f}")
print(f"Impostos (15%): R$ {impostos:,.2f}")
print(f"Valor Líquido:  R$ {valor_liquido:,.2f}")
print("-" * 30) 
