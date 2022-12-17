"""
Generators

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension... porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))
"""

# Poderíamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

print(getsizeof('Geek'))

print(getsizeof(9))

print(getsizeof('Geek'))

print(getsizeof(99293929392))

print(getsizeof(True))

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Set Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp}  bytes')
print(f'Set Comprehension: {set_comp} bythes')
print(f'Dictionary Comprehension: {dic_comp} bythes')
print(f'Generatoor Expression Comprehension: {gen} bythes')

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

    

