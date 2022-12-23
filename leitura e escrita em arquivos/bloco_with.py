"""
O bloco with

Passos para se trabalhar com arquivos
# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with.

"""

# O block with - Forma Pythônica de manipular arquivos

"""
as -> apelido

arquivo = open('texto.txt') 

with -> 'com' tal recurso "open('texto.txt')" chame ele de aqruivo

quando fora do contexto o que está dendtro do with não existe mais

ele abre e fecha o arquivo

"""
with open('texto.txt') as arquivo:
    print(arquivo.readline())
    print(arquivo.closed)  # Dentro do with ele ainda continua aberto

# Ele só é fechado quando sai do with
print(arquivo.closed)



