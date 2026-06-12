
# Variável global: x → está fora da função e pode ser acessada em qualquer parte do programa.

# Variável local: y → foi criada dentro da função teste() e só existe ali.

# Se tentarmos usar y fora da função: ocorrerá um erro (NameError), porque y não está definida no escopo global.

mensagem = "Olá"  # variável global

def juntar_palavra():
    palavra = "Mundo"  # variável local
    return mensagem + " " + palavra

print(juntar_palavra())   # funciona
print(mensagem)           # funciona
print('palavra')            # ERRO: palavra não existe fora da função
