fatias = int(input("Digite o número total de fatias de pizza: "))
numero_programadores = int(input("Digite o número de programadores: "))

if numero_programadores != 0:
    fatias_por_pessoa = fatias // numero_programadores
    sobra = fatias % numero_programadores
    print("Cada programador vai comer", fatias_por_pessoa, "fatias.")
    print("Vão sobrar", sobra, "fatias na caixa.")
else:
    print("Não é possível dividir entre 0 pessoas.")