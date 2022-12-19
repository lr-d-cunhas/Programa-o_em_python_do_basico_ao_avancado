"""
Len, abs, Sum, Round

# Len

len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.


"""

# Só para revisar

print(len('Rian Lucas'))

print(len([1, 2, 3, 4, 5]))

print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguitne

# Dunder len
print('Rian Lucas'.__len__())

"""
ABS

abs() -> Retorna o valor absoluto de um número inteiro ou rela.
DE forma básica, seria seu valor real sem o sinal
"""

print('# Exemplo Abs')

print(abs(-5))
print(abs(-3))
print(abs(-1))
print(abs(-20.12))

"""
sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna
a soma total dos elementos, incluindo o valor inicial

# OBS: O valor inicial default = 0
"""

# Exemplos Sum
print()

print(sum([1, 2, 3, 4, 5]))

# 5 é o valor inicial que passamos
print(sum([1, 2, 3, 4, 5], -5))

print(sum([3.1, 5.634]))

print(sum([1, 2, 3, 4]))

print(sum({1, 2, 3, 4}))

"""
# Round

round() -> Retorna um número arredondado para n digito de precisão após a casa decimal.
Se a precisão não for informada retorna o inteiro mais próximo da entrada.
"""
print()
# Exemplos Round

print(round(10.2))

print(round(10.5))

print(round(10.2323223123213, 2))

print(round(1.52323213213213123213134341, 2))
