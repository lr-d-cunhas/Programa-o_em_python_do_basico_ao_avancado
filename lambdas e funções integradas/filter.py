"""
Filter

filter() -> Serve para filtar dados de uma determinada coleção.

"""
# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(type(res))
print(list(res))

print(f'Novamente: {list(res)}')

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória


"""
Removendo valores faltantes
"""
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)
print(list(res))

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

res = filter(lambda pais: pais != '', paises)
print(list(res))

# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável.
# Retorna valores

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a filtragem.
# Sempre retorna ou true ou false

# Exemplos mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro Pizas"]},
    {"username": "Carla", "tweets": ["Eu adoro arroz"]},
    {"username": "Jeff", "tweets": []},
    {"username": "bobo123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu adoro bolacha", "Eu adoro vinagre"]},
]

print(usuarios)

# Filtrar os usuários que estão inativos no Twitter

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutura é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutura  é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

