"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escreve nele.

"""

# Exemplo de escrita - modo 'w' - write (escrita)

"""
Quando eu passo o modo 'w' se o nome do aqruivo não existe o arquivo é criado no SO. 

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro.
"""

"""
Abrindo um  arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
caso ele ja exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o conteúdo no arquivo anterior é perdido.
"""

# Forma Pythônica
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivos é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.')

# Forma tradicional de escrita em arquivo (não Pythônica)
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.')

arquivo.close()

with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)


with open('frutas.txt', 'w') as arquivo:
    while True:  # loop infinito, enquanto for true vamos ficar nesse loop
        fruta = input('informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break  # O brack só vai ser executado quando digitar sair
