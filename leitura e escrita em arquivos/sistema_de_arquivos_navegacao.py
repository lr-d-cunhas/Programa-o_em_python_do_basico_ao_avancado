"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.

os -> Operating System - Sistema Operacional

"""

# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trablaho corrente
# Retorna o path (caminho) absoluto
# print(os.getcwd())  # C:\Users\Rian\PycharmProjects\guppe

# Para mudar o diretório, podemos utilzar o chdir()

# os.chdir('..')

# print(os.getcwd())  # C:\Users\Rian\PycharmProjects

# os.chdir('..')

# print(os.getcwd())  # C:\Users\Rian

# os.chdir('..')

# print(os.getcwd())  # C:\Users

# os.chdir('..')

# print(os.getcwd())  # C:\

# os.chdir('..')

# print(os.getcwd())  # C:\

# Podemos checar se um diretório é absoluto ou relativo

# print(os.path.isabs('/User/Rian/'))  # True

# OBS para usuários Windows
# Se você, infelizmente, estiver utilizando um computador com Windows,
# terá que ter cuidado ao verificar diretórios.

# Tem que colocar duas barras para não achar que é um caracterie especial
# print(os.path.isabs('C:\\User\\geek'))

# Podemos identificar o sistema operacional com o módulo os
# print(os.name)  # posix (Linux e Mac), nt (Windows)


# Podemos ter mais detalhes no sistema opercaional
# não funcionou no meu windows
# print(os.uname())

# print(os.getcwd())  # C:\Users\Rian\PycharmProjects\guppe

# res = os.path.join(os.getcwd(), 'geek', 'university')

# os.chdir(res)

# print(os.getcwd())  #

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o
# diretório que será juntado ao atual.

# Podemos listar os arquivos e diretórios com o listdir()
# print(os.listdir('C:/'))

# print(len(os.listdir('C:/')))

# Podemos listar os arquivos e diretórios com mais detalhes com o scandir()

scanner = os.scandir()

arquivos = list(scanner)

# print(list(os.scandir('C:/')))

# print(list(os.scandir()))

# arquivos = list(os.scandir())

# print(arquivos)

# print(dir(arquivos[0]))

print(arquivos[0].inode())  #
print(arquivos[0].is_dir())  #
print(arquivos[0].is_file())  #
print(arquivos[0].is_symlink())  #
print(arquivos[0].path)  #
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].stat())

# st_size tamanho do arquivo em bytes

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo

scanner.close()




