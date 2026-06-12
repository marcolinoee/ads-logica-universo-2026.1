valor_hora = float(input("Digite o valor cobrado por hora: "))
horas_projeto = float(input("Digite a quantidade de horas do projeto: "))

valor_bruto = valor_hora * horas_projeto
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

print(f"Valor bruto: R$ {valor_bruto}")
print(f"Impostos: R$ {impostos}")
print(f"Valor líquido: R$ {valor_liquido}")