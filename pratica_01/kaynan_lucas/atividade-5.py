tamanho_mb = float(input("Digite o tamanho do arquivo (MB): "))
velocidade_mbps = float(input("Digite a velocidade da internet (Mbps): "))

tempo_segundos = tamanho_mb / (velocidade_mbps / 8)

minutos = int(tempo_segundos // 60)
segundos = int(tempo_segundos % 60)

print(f"{minutos} minutos e {segundos} segundos")