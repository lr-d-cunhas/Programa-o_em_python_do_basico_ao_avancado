"""
Argumentos Somente Posicionais
"""

# valor = '67.3'
# print(float(valor))

def cumprimenta_v1(nome):
    return f'Olá {nome}'

print(cumprimenta_v1('Geek'))
print(cumprimenta_v1(nome='Geek'))

def comprimenta_v2(nome, /):
    return f'Olá {nome}'

print(comprimenta_v2('Rian'))
# print(cumprimenta_v2(nome='Rian')) not

def cumprimenta_v3(nome, /, mensagem='Olá'):
    return f'{mensagem} {nome}'

print(cumprimenta_v3('Geek'))
print(cumprimenta_v3('University', mensagem='Hello'))
print(cumprimenta_v3('Felicity', 'Bem-vinda'))

# Todos os parâmetros antes da barra são somente posicionais
# Não queremos permitir que o usuário informe o parâmetro
def cumprimenta_v4(nome, mensagem='Olá', /):
    return f'{mensagem} {nome}'

print(cumprimenta_v4('Rian'))
print(cumprimenta_v4('Rian', 'Bem-vindo'))

# Podemos obrigar o usuário a informar o parâmetro
# Após o * todos os parâmetros são obrigatórios
def cumprimenta_v5(*, nome):
    return f'Olá {nome}'

print(cumprimenta_v5(nome='Geek'))
# print(cumprimenta_v5('Geek'))

# nome = somente posicional
# mensagem1 = comum tanto faz informar quanto não informar
# mensagem2 = é obrigatório informar
def cumprimentar_v6(nome, /, mensagem1='Olá', *, mensagem2):
    return f'{mensagem1} {nome} {mensagem2}'

print(cumprimentar_v6('Rian', mensagem1='Oi', mensagem2='short bvsp'))
print(cumprimentar_v6('Rian', mensagem2='short bvsp'))
