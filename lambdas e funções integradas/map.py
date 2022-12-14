"""
Map

Com map, fazemos mapeamento de valores para função.
"""

import math

def area(r):
    """Calcula a área de um círculo com raio 'r'."""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 4, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - Map

"""
Map é uma função que recebe dois parâmetros
1° a função
2° um iterável
Retorna um map object
"""

areas = map(area, raios)
print(type(areas))
print(list(areas))

# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map() depois da primeira utilização do resultao, ele zera.

"""
Para fixar - Map

Temos dados iteráveis:

dados: a1, a2, ..., an

temos uma função:

função: f(x)

# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função

O Map Object: f(a1), f(a2), f(a3), f(a4), f(...), f(an)
"""

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27),
           ('Londres', 22)]

print(cidades)

# f = 9/5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))

