# crm.py by Carlos (oncxr)

# Função que coleta os dados do cliente
def coletar_dados():
    nome_cliente = input("Digite seu nome: ")

    consumo_total = 0

    # Pede o valor individual mês por mês
    for i in range(1, 13):
        while True:
            try:
                valor = float(input(f"Digite o consumo do mês {i} (em kWh): "))

                if valor < 0:
                    print("Erro: O consumo não pode ser negativo. Tente novamente.")
                else:
                    consumo_total += valor
                    break

            except ValueError:
                print("Erro: Por favor, digite um número válido.")

    media_consumo = consumo_total / 12

    # Pede o HSP
    while True:
        try:
            hsp = float(input("Digite o HSP (Horas de Sol Pleno): "))

            if hsp <= 0:
                print("Erro: 0 HSP deve ser maior que zero para evitar divisões inválidas.")
            else:
                break

        except ValueError:
            print("Erro: Por Favor, digite um número válido para o HSP")

    # Pede a tarifa
    while True:
        try:
            tarifa = float(input("Digite a tarifa da concessionária (R$/kWh): "))

            if tarifa <= 0:
                print("Erro: A tarifa deve ser maior que zero.")
            else:
                break

        except ValueError:
            print("Erro: Por favor, digite um número válido para a tarifa.")

    # Pede a mão de obra
    while True:
        try:
            mao_obra = float(input("Digite o valor da mão de obra (R$): "))

            if mao_obra < 0:
                print("Erro: O valor não pode ser negativo.")
            else:
                break

        except ValueError:
            print("Erro: Por favor, digite um número válido.")


    # M2: Pergunta o tipo de sistema
    while True:
        print("\nTipo de sistema:")
        print("1 - On-Grid (conectado à rede, sem baterias)")
        print("2 - Off-Grid (isolado, com banco de baterias)")
        tipo_input = input("Escolha (1 ou 2): ").strip() # >>> Remove espaços em branco

        # Switch case pros sistemas (escolha e caso)
        match tipo_input:
            case "1":
                tipo_sistema = "On-Grid"
                break

            case "2":
                tipo_sistema = "Off-Grid"
                break

            # O equivalente de default em outras linguagens
            case _:
                print("Erro: Digite 1 para On-Grid ou 2 para Off-Grid")

    autonomia = None
    tensao = None

    if tipo_sistema == "Off-Grid":
        while True:
            try:
                autonomia = float(input("Digite a autonomia desejada (em dias sem sol): "))

                if autonomia <= 0:
                    print("Erro: A autonomia deve ser maior que zero.")
                else:
                    break

            except ValueError:
                print("Erro: Por favor, digite um número válido.")

        while True:
            tensao_input = input("Digite a tensão do sistema (24 ou 48): ").strip()

            if tensao_input == "24" or tensao_input == "48":
                tensao = float(tensao_input)
                break

            # Mostra erro caso a tensão não seja 24 ou 48
            print("Erro: A tensão deve ser 24 ou 48.")

    # Retorna os dados usados na função
    return (
        nome_cliente,
        media_consumo,
        hsp,
        tarifa,
        mao_obra,
        tipo_sistema,
        autonomia,
        tensao,
    )
