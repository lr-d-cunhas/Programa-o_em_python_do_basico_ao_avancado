"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir.
a -> Abre para escrita, adicionando o conteúdo ao final do aqruivo.
+ -> Abre para o modo de atualização: Leitura e Escrita. (temos o controle do cursor)

# OBS: Abrindo no mdo 'a' -> append, se o arquivo não existir será criado.
Caso exista, o novo conteúdo será adicionando ao final SEMPRE.

http://docs.python.org/3/library/functions.html#open
"""

# Exemplo x
"""
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo.\n')
except FileExistsError:
    print('Arquivo já existe')
"""

# Exemplo a
# a = mais interessante
"""
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
"""
"""
Com o modo 'a' não controlamos o cursor
"""
with open('outro.txt', 'a+') as arquivo:
    arquivo.seek(0)
    arquivo.write('1 topo!\n')
    arquivo.write('2 linha. \n')
    arquivo.write('3 uma linha. \n')
