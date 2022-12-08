"""
Funções com retorno

"""

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

# Exemplo função


def quadrado_de_7():
    print(7 * 7)


ret = quadrado_de_7()

print(f'Retorno {ret}')

"""
OBS: Funções Python que retornam valores, devem retornar estes valores a palabra reservada return 
"""


def quadrado_de_2():
    return 2*2


"""
OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar 
a execução da função para outras funções.
"""

ret2 = quadrado_de_2()
print(ret2)


# Refatorando a primeira função

def diz_bjs():
    return print('bjs')

print(diz_bjs())

"""
1 - Podemos ter, em uma função, diferentes returns
"""

# Exemplo 1


def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'O!'
    print('Estou sendo executado após o retorno...')  # Essa linha nunca sera executada


print(diz_oi())


# Exemplo 2


def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())


# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5


# num1, num2, num3, num4 = outra_funcao()
# print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))

# Vamos criar uma função para jogar a moeda

from random import random


def joga_moeda():
    # Gera um numero pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desenecessária.


def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else: # Esse else é desenecessario você pode remover ele
        return False


print(eh_impar())


