def ler_notas():
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    return nota1, nota2

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
     if media >= 7:
        return "Aprovado"
     else:
        return "Reprovado"
     
def exebir_resultados(media, situacao, nome):
    print("\n---boletim---")
    print(f"aluno: {nome}")
    print(f"média: {media}")
    print(f"situação: {situacao}")

nome = input("Digite o nome do aluno: ")
nota1, nota2 = ler_notas()
media = calcular_media(nota1, nota2)
situacao = verificar_situacao(media)
exebir_resultados(media, situacao, nome)