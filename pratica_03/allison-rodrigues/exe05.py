def ler_notas():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    return n1, n2

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_resultado(nome, media, situacao):
    print(f"\n--- Boletim ---")
    print(f"Aluno: {nome}")
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")

# Programa principal
nome_aluno = input("Digite o nome do aluno: ")
nota1, nota2 = ler_notas()
media = calcular_media(nota1, nota2)
situacao = verificar_situacao(media)
exibir_resultado(nome_aluno, media, situacao)
