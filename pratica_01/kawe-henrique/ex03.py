# Entrada de dados
total_fatias = int(input("Digite o número total de fatias de pizza: "))
num_programadores = int(input("Digite o número de programadores na equipe: "))

# Cálculos
# O operador // retorna apenas o número inteiro da divisão
fatias_por_pessoa = total_fatias // num_programadores

# O operador % retorna o que restou da divisão
sobra = total_fatias % num_programadores

# Saída de resultados
print("-" * 30)
print(f"Cada programador comerá: {fatias_por_pessoa} fatias")
print(f"Fatias que sobrarão na caixa: {sobra}")
print("-" * 30)