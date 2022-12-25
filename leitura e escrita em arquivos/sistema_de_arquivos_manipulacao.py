"""
Sistema de Arquivos - Manipulação
"""
import os

# Descobrindo se um arquivo ou diretório existe

# Arquivo
# print(os.path.exists('arquivo.txt'))  # False
# print(os.path.exists('frutas.txt'))  # False

# Diretório

# Path relativos
# print(os.path.exists('geek'))  # True
# print(os.path.exists('geek/university/geek3.py'))  # True
# print(os.path.exists('outro'))  # False

# Paths absolutos
# print(os.path.exists('/home/geek/university'))  # False
# print(os.path.exists('/home/geek/Imagens'))  # False
# print(os.path.exists('C://User'))  # True

# Criando arquivos e já fecha

# Forma 1
# open('arquivo-teste.txt', 'w').close()

# Forma 2
# open('arquivo-teste2.txt', 'a').close()

# Forma 3
# with open('arquivo-texte3.txt', 'w') as arquivo:
#     pass  # pass não faz nada simplesmente passa
# Se não colocar o pass ele vai reclamar que não tem identação

# Criando arquivos

# os.mknod('arquivo-teste4.txt')

# os.mknod('/home/geek/university')

# Se você estiver utilizando no Mac OS, pode haver um erro de PermissionError

# os.mkdir('templates')

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError

# OBS: Se não tivermos permissão para criar o diretório teremos um PermissionError

# Criando multi-diretórios (árvore de diretórios) Faça os diretórios
# os.makedirs('templates/geek/university')

# OBS: Se já existir, teremos um FileExistsError

# Se os arquivos já existirem não de erro
# Se existir, ignora
# os.makedirs('templates2/novo2/outro2', exist_ok=True)

# Renomear arquivos e diretórios

# templates2 > renomear > geek2

# Diretórios
# os.rename('templates2', 'geek2')

# OBS: Se o diretório não existir teremos um FileNotFoundError

# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSERror

# Arquivos
# os.rename('geek2/novo2/outro2/teste.txt', 'geek2/novo2/outro2/geek.txt')

# os.rename('frutas.txt', 'cesta.txt')

# ATENÇÃO!! Tome cuidado com comandos de deleção. Ao Deletarmos um arquivo de diretório, eles
# não vão para a lixeira. Eles somem

# os.remove('geek.txt')

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso,
# você terar erro.

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectioryError

# Remover diretórios vazios

# os.rmdir('templates')

# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError

# OBS: Se o diretório não existir teremos um FileNotFoundError

# Removendo uma árvore de diretórios

"""
for arquivo in os.scandir('geek2'):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)
"""

# Podemos remover uma árvore de diretórios vazios

# os.removedirs('geek2/outro/mais')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.

# ATENÇÃO: Ao remover arquivos e diretórios com Python eles não vão para a lixeira. Else vão ebora!

# sudo apt-get install lsb-core
# pip install send2trash


# Importando a biblioteca send2trash
# from send2trash import send2trash

# os.remove('cesta1.txt')  # Não vai para a lixeira. É deletado imediatamente

# send2trash('cesta2.txt')  # Vai para lixeira. Pode ser restaurado

# OBS: Se o arquivo não existir, teremos OSError

# send2trash('teste')  # Envia diretório também

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile
"""
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()
"""
# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando
# Um arquivo para escrevermos um texto. No final, usamos o input() só para  mantermos
# os arquivos temporários 'vivos' dentro dos blocos with.

# OBS: possivelmente, o código acima não irá funcionar se você estiver utilizando
# o Windows. Por conta desse sistema trabalhar de forma diferente com arquivos
# temporários.

# Criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso,
# utilizamos b''

"""
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()
"""

"""
arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)

print(arquivo.read())

input()

arquivo.close()
"""

