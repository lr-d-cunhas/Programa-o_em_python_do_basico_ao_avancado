"""
Ranges são utilizados para gerar sequências numéricas, não de forma aleatória.
mas sim de maneira especificada.

Formas gerais:

range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)

# Forma 2
range(valor_de_inicio, valor_de_parada)
for num in range(4, 11):
    print(num)

# Forma 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo Forma 3
for num in range(1, 10, 2):
    print(num)

# Exemplo forma 4
# Começa em 10, e vai decrementar em -1
for num in range(10, -1, -1):
    print(num)

"""

