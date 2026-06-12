fatias = int(input("Digite o total de fatias de pizza: "))
programadores = int(input("Digite o número de programadores: "))

fatias_por_pessoa = fatias // programadores
sobra = fatias % programadores

print(f"Cada programador vai comer {fatias_por_pessoa} fatias.")
print(f"Vão sobrar {sobra} fatias.")