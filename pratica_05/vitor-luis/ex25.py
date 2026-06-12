laboratorio = [
    ["L", "L", "O", "L", "M"],
    ["L", "M", "L", "O", "L"],
    ["O", "L", "L", "L", "L"],
    ["L", "L", "M", "L", "O"]
]

while True:
    print("\n--- MAPA DO LABORATÓRIO ---")
    print("    C0  C1  C2  C3  C4")
    
    for i in range(4):
        linha_formatada = "   ".join(laboratorio[i])
        print(f"F{i}:  {linha_formatada}")
    print("-" * 27)

    livres = 0
    ocupados = 0
    manutencao = 0
    
    for fileira in laboratorio:
        for computador in fileira:
            if computador == "L":
                livres += 1
            elif computador == "O":
                ocupados += 1
            elif computador == "M":
                manutencao += 1
                
    print("\n--- RESUMO DE OCUPAÇÃO ---")
    print(f"Computadores Livres (L): {livres}")
    print(f"Computadores Ocupados (O): {ocupados}")
    print(f"Em Manutenção (M): {manutencao}")
    print("-" * 26)

    print("\nDeseja ocupar um computador?")
    opcao = input("Digite 'S' para sim ou qualquer outra tecla para sair: ").upper()
    
    if opcao != 'S':
        print("\nPrograma encerrado. Até logo!")
        break
        
    fileira = int(input("\nDigite o número da fileira (0 a 3): "))
    coluna = int(input("Digite o número do computador/coluna (0 a 4): "))
        
    if fileira < 0 or fileira > 3 or coluna < 0 or coluna > 4:
        print("\nERRO: Posição fora dos limites do laboratório! Tente novamente.")
        continue
            
    status_atual = laboratorio[fileira][coluna]
        
    if status_atual == "M":
        print("\nERRO: Computador em MANUTENÇÃO. Não pode ser ocupado!")
    elif status_atual == "O":
        print("\nAVISO: Este computador JÁ ESTÁ OCUPADO!")
    elif status_atual == "L":
        laboratorio[fileira][coluna] = "O"
        print(f"\nSucesso! Computador na Fileira {fileira}, Coluna {coluna} agora está OCUPADO.")
