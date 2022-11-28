"""
Loop for

Loop -> Estrutura de reetição.
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < limitador; i++){
    //execução do loop
}
Python

for item in interavel;
    //Execução do loop

Utilizamos loops para iterar sore sequências ou sobre valores iteráveis

Exemplo de iteráveis
- String
    nome = 'Geek University'
- Lista
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
- Range
    numero = range(1, 10)
"""
nome = 'Rian Lucas'
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando em uma string)
# Pega cada uma das letras separadamente
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
# Para cada numero dessa lista imprime o numero
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
"""
range(valor_inicial, valor_final)

OBS: O valor final não é inclusivo. até o 9, não o 10
1
2
3
4
5
6
7
8
9
10 - Não
"""
for numero in range(1, 10):
    print(numero)

"""
Enumerate:

((0, 'R'), (1, 'i'), (2, 'a'), (3, 'n'))

Para cada sequência iteravel ele adiciona um índice 

nome = 'Rian'
for indice, v in enumerate(nome):
    print(nome[indice])

# _ discarta um valor, esse enumerate retorna 2 valores o índice e a letra
# descarto o índice e fico com a letra
for _, letra in enumerate(nome):
    print(letra)

# acesso ao indice e a letra
for valor in enumerate(nome):
    print(valor)

# acesso apenas ao índice
for valor in enumerate(nome):
    print(valor[0])

# Pergunta ao usuário quantas vezes deve rodar
qtd = int(input('Quantas vezes esse loop deve rodar?'))
for n in range(1, qtd+1):
    print(f'imprimindo{n}')

# Esse é top!!!
# Ele pergunta qual valor de um total ex: informe o valor 1/10, 2/10...
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

# Eu imprimo cada um dos caracteries sem pular linha, lado a lado
nome = 'Rian Lucas da Cunha Silva'
for letra in nome:
    print(letra, end='')
"""

# https://apps.timwhitlock.info/emoji/tables/unicode
# original: U+1F60D
# Modificado: U0001F60D
emoji = '\U0001F60D'
for num in range(1, 11):
    print(f'{emoji * num}')

