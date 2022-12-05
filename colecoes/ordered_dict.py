"""
Módulo Collections: Ordered Dict

OrderedDict -> É um dicionário, que nos garante a ordem de inserção dos elementos.

A performance melhor desempenho
"""
# Em um dicionáro, a ordem de inserção dos elementos não é garantida.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4,  'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

print(dicionario)

# Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4,  'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True/False?? = True, a ordem não importa

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # True/False?? = False, a ordem importa
