# motor_solar.py by Vitor (Vit0ncio)

# Função que calcula o consumo diário
def calc_consumo_diario(consumo_mensal):
    return consumo_mensal / 30


# Função que calcula o kWp
def pot_pico_kwp(consumo_diario, hsp):
    if hsp == 0:
        return None

    return consumo_diario / (hsp * 0.8)


# Função auxiliar que arredonda painéis e baterias para cima
def arredondar_cima(valor):
    if valor > int(valor):
        return int(valor) + 1

    return int(valor)


# Função que calcula os painéis
def calc_paineis(kwp_total, potencia_painel_kw):
    if potencia_painel_kw == 0:
        return None

    return arredondar_cima(kwp_total / potencia_painel_kw) # >>> Usa a função de arrendondamento para retorar o valor


# Função que calcula o custo total
def calc_custo_total(qtd_paineis, preco_painel, inversor, mao_obra):
    return (qtd_paineis * preco_painel) + inversor + mao_obra


# Função que calcula a economia
def calc_economia(consumo_mensal, tarifa):
    return consumo_mensal * tarifa


# Função que calcula o payback
def calc_payback(custo_total, economia_mensal):
    if economia_mensal <= 0:
        return None

    return custo_total / economia_mensal


# Função que calcula o banco de baterias
def calc_banco_bat(consumo_diario, autonomia, tensao):
    return (consumo_diario * 1000 * autonomia) / (tensao * 0.80)


# Função que calcula a quantidade de baterias
def calc_qtd_baterias(capacidade_total_ah, capacidade_bateria_ah):
    return arredondar_cima(capacidade_total_ah / capacidade_bateria_ah) # >>> Usa a função de arrendondamento para retorar o valor
