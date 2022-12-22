"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)
________________________
|Python|Módulos builtin|
------------------------
"""

# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())

# Importando todo o módulo

import random

print(random.random())

# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi

print(rdi(5, 89))

# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmos módulo
from random import (
    random,
    randint,
    shuffle,
    choice)

print(random())

print(randint(3, 7))

print()

lista = [1, 2, 3, 4]
shuffle(lista)
print(lista)

print()
print(choice('Lucas'))


