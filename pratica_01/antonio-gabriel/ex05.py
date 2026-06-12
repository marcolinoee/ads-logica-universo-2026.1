tamanho_arq_mb = int(input("Digite o tamanho do arquivo em 'MB': "))
velocidade_net_mbps = int(input("Digite a velocidade da sua internet em Mbps: "))

tempos_seg = tamanho_arq_mb / (velocidade_net_mbps / 8)
minutos =  int(tempos_seg // 60)
segundos = int(tempos_seg % 60)

print(f"{minutos} minutos e {segundos} segundos para o download ser concluído. ")