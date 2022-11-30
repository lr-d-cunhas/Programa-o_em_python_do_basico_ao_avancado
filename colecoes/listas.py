"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dados.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dados fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:
- Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []
"""
type([])
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['R', 'i', 'a', 'n', ' ', 'L', 'u', 'c', 'a', 's']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista
num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas

"""
Para adicionar elementos em listas, utilizamos a funlção append

OBS: Com append, nós só conseguios adicionar 1 elementos por vez

se tentar
    - lista1.append(12, 34, 56) # Erro
"""
print(lista1)
lista1.append(42)
print(lista1)

if 22 in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista6 = [22, 23, 24, 25, 26]
lista6.append([0, 1, 2]) # coloca a lista como elemento único (sublista)

if [0, 1, 2] in lista6:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

# Adicionando elementos em uma lista
lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional á lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntar duas listas
# lista7 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Isso gera o mesmo resultado do .reverse
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista7 = lista2.copy()
print(lista7)

# Tamanho da lista (elementos da lista)
print(len(lista1))

# Remover o último elemento de uma lista
# Obs: o pop também retorna o último elemento que ele removeu
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# Obs: os elementos á direita deste índice serão deslocados para a esquerda;
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca o cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 42421312]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1
# Ele passa em todos os elementos da lista
soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)
