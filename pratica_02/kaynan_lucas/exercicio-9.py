salario = float(input("Digite o salário: "))

if salario <= 1500:
    reajuste = salario * 0.15
elif salario <= 3000:
    reajuste = salario * 0.10
else:
    reajuste = salario * 0.05

novo_salario = salario + reajuste

print("Novo salário:", novo_salario)