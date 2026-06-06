salario = float(input("Digite o salário atual: "))

if salario <= 1500:
    percentual = 15
elif salario <= 3000:
    percentual = 10
else:
    percentual = 5

reajuste = salario * (percentual / 100)
novo_salario = salario + reajuste

print("Salário original: R$", salario)
print("Percentual aplicado:", percentual, "%")
print("Novo salário: R$", novo_salario)