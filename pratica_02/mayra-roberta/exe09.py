salario = float(input("Digite o salário: "))

if salario <= 1500:
    novo_salario = salario + (salario * 0.15)
elif salario <= 3000:
    novo_salario = salario + (salario * 0.10)
else:
    novo_salario = salario + (salario * 0.05)

print("Novo salário: R$", novo_salario)