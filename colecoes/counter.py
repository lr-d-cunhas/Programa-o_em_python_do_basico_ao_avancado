"""
Módulo Collections - Counter

Collections -> High-performance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter
que é parecido com um dicionáro, contendo como chave o elemento da lista passado como parâmetro e como valor a
quantidade de ocorrências desse elemento.


"""

# Realizando o import

from collections import Counter


# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 2, 3, 5, 5, 5, 5, 5, 4, 5, 4, 4, 11, 12, 44, 55, 12]

# Utilzando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({5: 6, 1: 5, 2: 4, 3: 4, 4: 3, 12: 2, 11: 1, 44: 1, 55: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências

# Exemplo 2

print(Counter('Rian Lucas da Cunha Silva'))
# Counter({'a': 5, ' ': 4, 'i': 2, 'n': 2, 'u': 2, 'R': 1, 'L': 1, 'c': 1, 's': 1, 'd': 1, 'C': 1, 'h': 1, 'S': 1, 'l': 1, 'v': 1})

# Exemplo 3

texto = """
Suponha que tendo-se uma função u a qual descreve a temperatura em uma determinada posição (x, y, z). Esta função irá 
alterar-se com o tempo na medida em que o calor se dissipa através do espaço. 
A equação do calor é usada para determinar a alteração na função u no tempo. A imagem acima é animada e tem uma descrição
das alterações do trajeto do calor ao longo do tempo numa barra de metal. Uma das interessantes propriedades da equação 
do calor é o princípio do máximo o qual afirma que o valor máximo de u seja anterior no tempo que a região de interesse 
ou na borda da região de interesse. Isto é, essencialmente, afirmar que a temperatura vem tanto de uma fonte ou de anteriores,
no tempo, porque permeia calor, mas não é criado do nada. Esta é uma propriedade das equações diferenciais parciais parabólicas 
e não é difícil de provar-se matematicamente (ver abaixo).
A equação do calor é usado em probabilidade e descreve passeios aleatórios. É também aplicada em matemática financeira por esta razão.
"""

palavras = texto.split()

# print(palavras)

# Ele vai pegar a ocorrência de cada palavra no texto

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))

