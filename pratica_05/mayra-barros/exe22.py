# Matriz irregular
dados = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

# Versão corrigida
for i in range(len(dados)):
    for j in range(len(dados[i])):  # usa o tamanho real da linha
        print(dados[i][j])


# Por que range(3) não é seguro nesse caso?
# Porque nem todas as linhas têm exatamente 3 elementos.
# Se usarmos range(3), ao acessar uma linha menor (como a segunda, que tem apenas 2 elementos),
# o programa tentará acessar índices inexistentes e gerará um IndexError.
# Usar len(dados[i]) garante que percorremos apenas os índices válidos de cada linha.
