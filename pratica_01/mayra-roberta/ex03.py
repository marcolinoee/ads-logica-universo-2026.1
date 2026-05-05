fatias = int(input("Quantas fatias de pizza no total? "))
pessoas = int(input("Quantas pessoas comerão? "))

fatias_por_pessoa = fatias // pessoas
sobra = fatias % pessoas

print(f"\n ---resultado---")
print(f"Cada pessoa comerá {fatias_por_pessoa} fatias.")
print(f"Sobram {sobra} fatias.")
