fatias = int(input("Quantas fatias de pizza? "))
pessoas = int(input("Quantas pessoas? "))

fatias_por_pessoa = fatias // pessoas
sobra = fatias % pessoas

print(f"\n ---resultado---")
print(f"Cada pessoa recebe {fatias_por_pessoa} fatias.")
print(f"Sobram {sobra} fatias.")
