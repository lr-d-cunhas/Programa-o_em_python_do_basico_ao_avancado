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

# Exemplo 1 - Utilizando for
# Ele passa em todos os elementos da lista
soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

"""
Você vai escrevendo os valores para adicionar na lista quando tiver digitado todos
digite sair 

ele vai appendando os valores que você for adicionando
"""

while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" paraa sair:')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
# Valores fixos ou variáveis
numeros = [1, 2, 3, 4, 5]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

#          0         1         2         3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense na lista como um círculo, onde
# o final de um elemento está ligado ao início da lista

print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
#  print(cores[-5])  # Erro, pois não existe índice -5

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outross métodos não tão importantes mas também úties

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10]

# Em qual índice da lista está o valor 6?
print(numeros.index(6))

# em qual índice da lista está o valor 9?
print(numeros.index(9))

# print(numeros.index(19)) # Gera ValueError

# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

# OBS: Retorna o índice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))  # buscando a partir do índice 1
print(numeros.index(5, 2))  # buscando a partir do índice 2
print(numeros.index(5, 3))  # buscando a partir do índice 3
# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))  # Buscar o índice do valor 8, entre os índices 3 e 6

# Revisão de slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista - com o parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:])  # Iniciando no índice 1 e pegando todos os elementos restantes
print(lista[::])  # Pegando todos os elementos

# Trabalhando com slice de lista com parâmetro 'fim'

print(lista[:2])  # começa em 0, pega até o índice 2 - 1
print(lista[:4])  # começa em 0, pega até o indice 3 - 1
print(lista[1:])  # começa em 0, pega até o índice 3 - 1

# Trabalhando com slice de lista com o parâmetro 'passo'

print(lista[1::2])  # Começa em 1, vai até o final, de 2 em 2
print(lista[::2])  # Começa em 0, vai até o final, de 2 em 2

# Invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1], = nomes[1], nomes[0]
print(nomes)

# ou

nomes.reverse()
print(nomes)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista))  # máximo valor
print(min(lista))  # mínimo valor
print(len(lista))  # tamanho da lista

# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tuple))

# Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos mais elementos para desempacotar do que variáveis para receber os valores, tereos ValueError

# Copiando uma lista para outra (Shallow copy e Deep Copy)

# Forma 1 - Deep copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista,
# mas elas ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra.
# Isso em Python é chamado de Deep Copy (cópia profunda)

# Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista  # cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# após relizar modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow copy
