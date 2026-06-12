tamanho_mb = float(input("Digite o tamanho do arquivo (MB): "))
velocidade_mbps = float(input("Digite a velocidade da internet (Mbps): "))

# Convertendo a velocidade (Mbps -> MB/s)
velocidade_mb_s = velocidade_mbps / 8

# Calculando o tempo total em segundos
tempo_segundos = tamanho_mb / velocidade_mb_s

# Convertendo para minutos e segundos
minutos = int(tempo_segundos // 60)
segundos = int(tempo_segundos % 60)

# Mostrando o resultado
print(f"{minutos} minutos e {segundos} segundos")