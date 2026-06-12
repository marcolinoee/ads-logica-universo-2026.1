fatias = int(input("Digite o total de fatias: "))
pessoas = int(input("Digite o número de programadores: "))

fatias_por_pessoa = fatias // pessoas
sobra = fatias % pessoas

print(f"Cada pessoa come {fatias_por_pessoa} fatias")
print(f"Sobram {sobra} fatias")