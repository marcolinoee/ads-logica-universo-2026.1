from produtos import cadastrar_produto
from motor_vendas_peps import processar_venda
from dashboards_relatorios import (
    curva_abc,
    relatorio_estoque_minimo,
    inventario_geral,
    relatorio_lotes
)



while True:


    print("""
=========================
     ERP ESTOQUE
=========================

1 - Cadastrar produto
2 - Realizar venda
3 - Curva ABC
4 - Estoque mínimo
5 - Inventário geral
6 - Relatório de lotes
0 - Sair

""")


    opcao = input("Escolha uma opção: ")



    match opcao:


        case "1":

            cadastrar_produto()



        case "2":

            codigo = int(
                input("Código do produto: ")
            )


            quantidade = int(
                input("Quantidade vendida: ")
            )


            processar_venda(
                codigo,
                quantidade
            )



        case "3":

            curva_abc()



        case "4":

            relatorio_estoque_minimo()



        case "5":

            inventario_geral()



        case "6":

            relatorio_lotes()



        case "0":

            print("Encerrando sistema...")
            break



        case _:

            print("Opção inválida!")
            