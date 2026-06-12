Alteração de valores em uma matriz

 Explicação:

A matriz é uma lista de listas, então notas[linha][coluna] acessa diretamente a posição desejada.

Alteramos valores específicos com atribuição simples.

No desafio, o programa pede ao usuário índices e valor, permitindo atualizar dinamicamente qualquer célula.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Contando números pares e ímpares

Explicação:

Usamos % 2 para verificar se o número é par (== 0) ou ímpar (!= 0).

Mantemos dois contadores (pares e impares).

No desafio, criamos uma lista pares_encontrados para armazenar todos os números pares encontrados.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Maior valor e sua posição

 Explicação:

Usamos range(len(...)) para percorrer linhas e colunas.

Guardamos tanto o maior valor quanto sua posição (linha e coluna).

A resposta final mostra exatamente onde o valor está.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Grade de assentos: reserva de posição

Explicação:

A matriz sala representa os assentos, com "L" para livre e "O" para ocupado.

A função mostrar_sala imprime a sala em formato de tabela, facilitando a visualização.

O programa pede linha e coluna, verifica se estão dentro dos limites e atualiza o estado do assento.

O desafio extra foi implementado: o usuário pode fazer várias reservas até digitar -1 para sair.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Aula com mais faltas

Explicação:

Cada coluna representa uma aula.

O laço externo percorre as colunas, e o interno percorre os estudantes daquela aula.

Contamos as faltas ("F") e verificamos qual coluna teve o maior número.

No final, mostramos o índice da aula e a quantidade de faltas.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Jogada simples no jogo da velha

Explicação:

O programa pede linha e coluna (0 a 2) e o símbolo (X ou O).

Se o símbolo for inválido, mostra mensagem de erro.

Se a posição estiver vazia (" "), a jogada é realizada.

Caso contrário, exibe Jogada inválida.

Ao final, o tabuleiro atualizado é mostrado.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Depuração: matriz irregular

Explicação:

A matriz é irregular, ou seja, cada linha pode ter um número diferente de elementos.

O erro acontece porque o código original fixava range(3), assumindo que todas as linhas tinham 3 elementos.

A solução é usar len(dados[i]), que adapta o laço ao tamanho real da linha.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Depuração: inicialização incorreta

 Explicação:

O erro acontece porque o operador * duplica referências, não cria listas independentes.

Na versão corrigida com compreensão de listas, cada linha é criada separadamente, evitando o compartilhamento de referência.

Assim, ao alterar uma célula, apenas aquela célula é modificada.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Mini-projeto: sistema simples de boletim

 Explicação:

Cada estudante tem 4 notas armazenadas em uma matriz.

Calculamos a média com sum(...) / len(...).

Classificamos conforme as regras: Aprovado, Recuperação ou Reprovado.

Guardamos o estudante com maior e menor média para exibir no final.

O relatório mostra todos os estudantes e depois os extremos da turma.

Esse mini-projeto integra listas, matrizes, médias, condições e relatórios, simulando um sistema simples de boletim escolar.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Mini-projeto: mapa de ocupação de laboratório

Explicação:

"L" = livre, "O" = ocupado, "M" = manutenção.

A função exibir_mapa mostra o laboratório em formato de tabela.

A função contar_estados calcula quantos computadores estão em cada estado.

O programa valida a posição escolhida pelo usuário, impede ocupar máquinas em manutenção e atualiza o mapa.

Esse mini-projeto é ótimo porque integra matrizes, contagem, validação de limites e atualização de estados, simulando um sistema real de ocupação de laboratório.