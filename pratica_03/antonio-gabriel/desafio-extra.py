# Desafio extra
# Sistema de cadastro de dados de aluno

#FUNÇÃO PARA LER NOME DO ALUNO
def nome_aluno():
    nome = input("Digite o nome do aluno: ")
    return nome

#FUNÇÃO PRA LER AS NOTAS
def ler_notas():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    return n1, n2
    
#FUNÇÃO PRA CALCULAR A MÉDIA 
def calcular_media(n1,n2):
    return(n1 + n2) / 2
    
#FUNÇÃO PRA VERIFICAR A SITUAÇÃO 
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

#FUNÇÃO PARA EXIBIR O RELATÓRIO FINAL
def relatorio_final(nome, media, situacao):
    
    print(f"Aluno: {nome} ")
    print(f"Média: {media} ")
    print(f"Situação: {situacao} ")
    
#PROGRAMA PRINCIPAL

nome = nome_aluno()

n1, n2 = ler_notas()

media = calcular_media(n1, n2)

situacao = verificar_situacao(media)

relatorio_final(nome, media, situacao)