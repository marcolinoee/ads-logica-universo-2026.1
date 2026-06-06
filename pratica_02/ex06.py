nota = float(input("Digite uma nota (0 a 10): "))

while nota < 0 or nota > 10:
    nota = float(input("Invalido! Digite novamente: "))

print("Nota válida:", nota)