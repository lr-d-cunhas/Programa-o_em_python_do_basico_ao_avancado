"""
Seek e cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.


"""

arquivo = open('texto.txt')

# print(arquivo.read())

"""
seek() -> A função seek() é utilizada para movimentação do cursor  pelo arquivo. Ela recebe
um parâmetro que indica onde queremos colocar o cursor.
"""
# Movimento o cursor pelo arquivo com a função seek()
# arquivo.seek(0)

# print(arquivo.read())

# arquivo.seek(50)  # Seria o inicio da leitura do cursor

# print(arquivo.read())

"""
Em muitos casos teremos que fazer a leitura do arquivo linha a linha

readline() -> Função que lê o arquivo linha a linha
"""
# print(arquivo.readline())

# print(arquivo.readline())

# print(arquivo.readline())

# ret = arquivo.readline()

# print(type(ret))

# print(ret)

# print(ret.split(' '))
"""
# readlines() -> coloca as linhas dentro de uma lista, 
"""

# linhas = arquivo.readlines()

# prin(len(linhas))

"""
OBS: Quando abrirmos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco do computador e o seu programa. Essa conexão é chamada de straming.
Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos a função
close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo

3 - Fechar o arquivo
"""

# 1 - Abrir o arquivo;
arquivo = open('texto.txt')

# 2 - Trabalhar o arquivo;
print(arquivo.read())

print(arquivo.closed)  # |False| Verifica se o arquivo está aberto ou fechado

# 3 - Fechar o arquivo;
"""
Evitar problemas
"""
arquivo.close()

print(arquivo.closed)  # |True| Verifica se o arquivo está aberto ou fechado

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(50))


