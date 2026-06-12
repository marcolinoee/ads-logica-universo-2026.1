tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_internet = float(input("Digite a velocidade da internet em Mbps: "))

tempo_segundos = (tamanho_arquivo * 8) / velocidade_internet

minutos = int(tempo_segundos // 60)
segundos = int(tempo_segundos % 60)

print(f"Tempo estimado de download: {minutos} minutos e {segundos} segundos.")