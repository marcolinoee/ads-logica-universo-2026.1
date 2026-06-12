valor_hora = float(input('Informe o valor cobrado por hora: '))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas: '))

valor_bruto = valor_hora * horas_trabalhadas
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

print(f" Valor Bruto: R$ {valor_bruto:.2f}\n Valor dos Impostos: R$ {impostos:.2f}\n Valor Líquido: R$ {valor_liquido:.2f}")
