"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.

"""

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando todo o módulo (Não recomendado).

import random

# random() -> Gera um número pseudo-aleatório entre 0 e 1.

# Ao  realizar o import de todo o módulo, todas as funções atributos, classes e propriedes que estiverem
# dentro do módulo ficarão disponíveis (Ficarão em Memória). Caso vocÊ saiba quais funções você precisa utilizar
# deste  módulo, então esta não seria a forma ideial de utilização. Nós veremos uma forma melhor na Forma 2.

print(random.random())

# Veja que para utilizar a função random() do  pacote random, nós colocamos o nome do pacote, e o nome da função
# separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random é
# apenas uma função dentro do módulo random.

# Forma 2 - Importando uma função específica do módulo (Forma recomendada)

from random import random

# No import acima, estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())

# uniform() ->Gerar um número real pseudo-aleatório entre os valores estabelecidos
print()

from random import uniform

for i in range(10):
    # Podemos especificar valores
    print(uniform(-100, 100))  # 7 não é incluído. # Gerar valores aleatórios

# randint() -> Gera valores pseudo-aleatórios entre os valores esptabelecidos.
print()

from random import randint

# Gerador de apostas para a mega-sena
for i in range(6):
    # Gera números de 1 até 60 inteiros 'não pega 60'
    print(randint(1, 61), end=', ')  # ao invés de pular uma linha ele coloca ','

print()

# choice() -> Mostra um valor aleatório entre um iterável.
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

print(choice('Rian Lucas'))


from random import shuffle

# Shuffle() -> Tem a função de embaralhar dados
print()

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas)

print(cartas.pop())

