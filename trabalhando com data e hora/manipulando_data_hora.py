"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime
"""

import datetime

"""
# print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

# Retorna a data e hora corrente

print(datetime.datetime.now())  # 2022-12-31 11:34:04.590821  BR 21/12/2018

# datetime.datetime(year, month, daty, hour, minite, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)  # 2022-12-31 11:39:09.882814

# Alterar o horário para 16 horas, 0 minuto, 0 segund, 0 microsegundo
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)  # 2022-12-31 16:00:00
"""


# Recebendo dados do usúario e convertendo para data

"""
evento = datetime.datetime(2019, 1, 1, 0)

print(type(evento))

print(type('31/12/2018'))

print(evento)

nascimento = input('Informe sua data de nascimento: (dd/mm/yy)')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))
"""

# Acesso individual dos elementos de data e hora

evento = datetime.datetime.now()

print(evento.year)  # ano
print(evento.month)  # mês
print(evento.day)  # dia
print(evento.hour)  # hora
print(evento.minute)  # minute
print(evento.second)  # segundo
print(evento.microsecond)  # microsegundo

print(dir(evento)) # Métodos que ainda podem ser aplicados (DIR)
