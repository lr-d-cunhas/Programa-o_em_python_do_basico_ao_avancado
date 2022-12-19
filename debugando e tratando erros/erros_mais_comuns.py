"""
Erros mais comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução
do nosso código.

Os erros mais comuns:

# Exemplos SytaxError

SytaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja
você escreveu algo que o python não reconhece como parte da linguagem.

a)
def funcao:
    print('Rian Lucas')

b)
def = 1

c)
return

# NameError -> Ocorre quando uma variável ou função não foi definida

a)
print(geek)

b)
geek()

c)
a = 18
if a < 10:
    msg = 'É maior que 10'
    # msg não vai existir
print(msg)

# TypeError

Ocorre quando uma função/operação/ação é aplicada a um tipo errado

Exemplos TypeError

a)
print(len(5))

b)
print('Geek' + [])

# IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado
indexado utilizando um índice inválido

Exemplos IndexError

a)
lista = ['Geek']
print(lista[2])

b)
lista = ['Geek']
print(lista[0][10])

# ValueError ->ocorre quando uma função/operação built-in (integrada)
recebe um argumento com tipo correto mas valor inapropriado

Exemplo ValueError

a)
print(int('Geek'))

# KeyError - Ocorreq uando tentamos acessar um dicionário com chave que não existe

a)
dic = {'python': 'university'}
print(dic['geek'])

# AtributeError -> Ocorre quando uma variável não tem um atributo/função

a)
tupla = (11, 2, 31, 4)
print(tupla.sort())
print(tupla)

b)

# IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

Exemplos IndentationError

a)
def nova():
print('Geek')

b)
for i in range(10):
i + 1


OBS: Exeptions e Erros são sinônimos na programação

OBS: Importante ler e prestar atenção na saída de erro.

"""




