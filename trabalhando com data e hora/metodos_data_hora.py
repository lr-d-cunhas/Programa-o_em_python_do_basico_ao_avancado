"""

Métodos de Data e Hora

"""

import datetime

"""
# Com now() podemos especificar um timezone (Fuso Horário)
agora = datetime.datetime.now()  # now == agora
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()  # now == hoje
print(hoje)
print(type(hoje))
print(repr(hoje))
"""

"""
# Mudanças ocorrendo à meia-noite combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))
"""

# Encontrar o dia da semana. weekday()

"""
Os dias da semana do método weekday() começam em 0, sendo esta a segunda-feira

0 - Segunda-feira (Monday)
1 - Terça-feira (Tuesday)
2 - Quarta-feira (Wednesday)
3 - Quinta-feira (Thursday)
4 - Sexta-feira (Friday)
5 - Sábado (Saturday)
6 - Domingo (Sunday)

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())
"""

"""
aniversario = input('Qual sua data de nascimento? dd/mm/yyyy: ')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma terça-feira')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma quinta-feira')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma sexta-feira')
elif aniversario.weekday() == 5:
    print('Você nasceu em um sábado')
elif aniversario.weekday() == 6:
    print('Você nasceu em um domingo')

"""

"""
# Formatando datas/horas com strftime (String Format Time)
# dd/mm/yyyy hora:minuto

hoje = datetime.datetime.today()

print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')  # 01/01/2023
hoje_formatado2 = hoje.strftime('%d/%B/%Y')  # 01/January/2023
hoje_formatado3 = hoje.strftime('%d/%b/%Y')  # 01/Jan/2023

print(hoje_formatado)
print(hoje_formatado2)
print(hoje_formatado3)

#  https://docs.python.org/3/library/datetime.html

def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.monty == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'

print(formata_data(hoje))
"""

"""
did not work

from textblob import TextBlob

def formata_data(data):
    return f'{data.day} de {TextBlob(data.strftime("%B")).translate(to="pt-br")} de {data.year}'

hoje = datetime.datetime.today()

print(formata_data(hoje))
"""

"""
nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')

print(nascimento)

nascimento = input('Qual sua data de nascimento? (dd/mm/yyyy): ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)

# Somente a hora

almoco = datetime.time(12, 30, 0)

print(almoco)
"""

# import timeit

# Marcando tempo de execução no nosso código com timeit

# Loop for
# .join concatenar com traço '-'

"""
>>> "-".join((str(n) for n in range(100))) 
'0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21
-22-23-24-25-26-27-28-29-30-31-32-33-34-35-36-37-38-39-
40-41-42-43-44-45-46-47-
4

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comphension
tempo2 = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo2)
"""

import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print(timeit.timeit(functools.partial(teste, 2), number=10000))

