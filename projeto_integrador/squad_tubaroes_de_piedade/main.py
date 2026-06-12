# main.py by Arthur (arthurrqueiroz)

# Importação de variáveis/funções dos arquivos
from crm import coletar_dados
from motor_solar import * # >>> O '*' serve pra importar TUDO do motor_solar
from proposta import imprimir_relatorio
from catalogo_poo import paineis, inversores, baterias, ProjetoFotovoltaico

# Exibe uma lista do catálogo formatada no terminal
def exibir_catalogo(titulo, lista):
    print("\n" + "=" * 45)
    print(f"{titulo:^45}")
    print("=" * 45)
    for i, item in enumerate(lista, 1):
        print(f"  {i}. {item.modelo:<28} R$ {item.preco:.2f}")
    print()


# Pede para o usuário escolher um item da lista pelo número
def escolher_do_catalogo(lista, nome_item):
    while True:
        try:
            opcao = int(input(f"Escolha o número do {nome_item}: "))

            # Garante que a opção esteja dentro dos limites da lista
            # O 'if 1' garante que o usuário não digitou zero
            # O 'opcao <= len(lista)' garante que a opção escolhida não seja maior
            # que a quantidade de produtos na lista
            if 1 <= opcao <= len(lista):
                return lista[opcao - 1] # >>> Retorna o item escolhido menos 1, pois o índice começa em zero, e os itens são numerados de 1 pra cima
            print(f"Erro: Escolha um número de 1 a {len(lista)}.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")


# Função principal
def main():
    print("\n" + "=" * 45)
    print(f"{'SIMULADOR FOTOVOLTAICO':^45}")
    print("=" * 45 + "\n")

    # Coleta dados básicos do cliente via crm.py
    (
        nome_cliente,
        media_consumo,
        hsp,
        tarifa,
        mao_obra,
        tipo_sistema,
        autonomia,
        tensao,
    ) = coletar_dados()

    # M2: Exibe catálogo de painéis e deixa o usuário escolher
    exibir_catalogo("CATÁLOGO DE PAINÉIS", paineis)
    painel_escolhido = escolher_do_catalogo(paineis, "painel")

    # M2: Exibe catálogo de inversores e deixa o usuário escolher
    exibir_catalogo("CATÁLOGO DE INVERSORES", inversores)
    inversor_escolhido = escolher_do_catalogo(inversores, "inversor")

    # Cálculos do motor solar
    consumo_diario = calc_consumo_diario(media_consumo)
    pot_pico = pot_pico_kwp(consumo_diario, hsp)
    qtd_paineis = calc_paineis(pot_pico, painel_escolhido.potencia_kw)

    if qtd_paineis is None:
        print("Erro no cálculo dos painéis.")
        return

    economia = calc_economia(media_consumo, tarifa)

    # Variáveis para Off-Grid (padrão: sem baterias)
    bateria_escolhida = None
    qtd_baterias = 0
    custo_baterias = 0

    # M2: Se Off-Grid, exibe catálogo de baterias e calcula o banco
    if tipo_sistema == "Off-Grid":
        exibir_catalogo("CATÁLOGO DE BATERIAS", baterias)
        bateria_escolhida = escolher_do_catalogo(baterias, "bateria")

        # Calcula a capacidade total necessária em Ah
        capacidade_total_ah = calc_banco_bat(consumo_diario, autonomia, tensao)
        qtd_baterias = calc_qtd_baterias(capacidade_total_ah, bateria_escolhida.capacidade_ah)

        custo_baterias = qtd_baterias * bateria_escolhida.preco

    # Custo total incluindo baterias (se Off-Grid)
    custo_total = (
        calc_custo_total(qtd_paineis, painel_escolhido.preco, inversor_escolhido.preco, mao_obra)
        + custo_baterias
    )
    payback = calc_payback(custo_total, economia)

    projeto = ProjetoFotovoltaico(
        cliente = nome_cliente,
        painel = painel_escolhido,
        inversor = inversor_escolhido,
        bateria = bateria_escolhida,
    )

    projeto.kwp_total = pot_pico
    projeto.qtd_paineis = qtd_paineis
    projeto.qtd_baterias = qtd_baterias
    projeto.custo_total = custo_total
    projeto.economia_mensal = economia
    projeto.payback = payback


    # M2: Chama proposta.py para imprimir o ticket final formatado
    imprimir_relatorio(projeto, mao_obra, tipo_sistema)


# Inicia a função
main()
