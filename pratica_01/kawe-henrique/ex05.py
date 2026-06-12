# Solicita os dados ao usuário
tamanho_mb = float(input("Digite o tamanho do arquivo (MB): "))
velocidade_mbps = float(input("Digite a velocidade da internet (Mbps): "))

# Regra de Negócio: Calcula a velocidade em Megabytes por segundo
velocidade_mb_s = velocidade_mbps / 8

# Calcula o tempo total em segundos
tempo_segundos = tamanho_mb / velocidade_mb_s

# Converte para minutos inteiros e segundos restantes
minutos_inteiros = int(tempo_segundos // 60)
segundos_restantes = int(tempo_segundos % 60)

# Saída formatada
print(f"{minutos_inteiros} minutos e {segundos_restantes} segundos")