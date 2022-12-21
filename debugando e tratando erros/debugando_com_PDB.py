"""
Debugando com PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inseto


"""

"""
# OBS: A utilização do print() para debugar código é uma pratica ruim

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


# print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando
# o PDB - Pythoon Debugger

# Exemplo com o PyCharm

print(dividir(4, 0))
"""

"""
# Exemplo com o PDB - Python Debugguer  - Exemplo 1

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + 'faz o curso' + curso
print(final)
"""

"""
# Exemplo com o PDB - Python Debugger - Exemplo 2 

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + 'faz o curso' + curso
print(final)

# Por quê utilizar este formato?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
# no início do arquivo. Por isso, ao invés de colocarmos o import do pdb no início do arquivo
# nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.
"""

"""
# Exemplo com o PDB - Python Debugger - Exemplo 2

# * A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
# incoporado como função built-in (integrada) chamada breakpoint()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + 'faz o curso' + curso
print(final)
"""

# OBS: Cuidado com conflito entre nomes de variáveis e os comandos do pdb

# Como os nomes das variáveissão os mesmos do comando do pdb, devemos utilizar o comando p para imprimir
# as variáveis. Ou seja: p nome_da_variavel

# Nada de colocar nomes não represenetatitvos em variáveis. Sempre optar por nomes significativos.

