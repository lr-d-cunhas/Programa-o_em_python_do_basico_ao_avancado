"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Diconários são coleções do tipo chave/valor

Dicionários são representados por chaves {}.

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

"""
# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='paraguay')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chava, da mesma forma que lista/tupla
print(paises['br'])
# print(paises['ru'])

# OBS: Caso tentamos fazer um acesso utilizando uma chava que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendado

print(paises.get('br'))
print(paises.get('ru'))  # Quando não tiver o dado, ele retorna none, quando usamos o .get

"""
Pega pra mim o valor da chave ru, caso não encontre coloque 'o outro valor' no lugar
dessa forma a variável pais sempre vai ter um valor

# Lembrando que ele busca a chave 'ru'

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não 
será gerado KeyError

"""
pais = paises.get('ru', 'Não encotrado')
print(f'Encontrei o país {pais}')

# Verificar se determinado chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

"""
Podemos utulizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, diconário, como 
Tuplas por exemplo são bastante interessantes de serem utilizadas como chaava de dicionários pois as mesmas
são imutáveis
"""
localidades = {
    (35.12323, 23.23123): 'Escritório em Tókio',
    (235.12323, 13.22323): 'Escritório em Londres',
    (325.132323, 21323.3232): 'Escritório em Rio de Janeiro'
}
print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev':120, 'mar':300}
print(receita)
print(type(receita))

# Forma 1

receita['abr'] = 350
print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado)  # receita.update('mai' : 500)

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# CONCLUSÃO 1: A forma de adicionar elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários NÃO podemos ter chaves repetidas.

# Remover dados de um dicionário

print(receita)

# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita['fev']

print(receita)

# Se a chave  não existir será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado.

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

"""
Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;

"""

# Poderíamos utilizar uma Lista para isso? Sim

carrinho = []

produto1 = ['Paystation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o índice de cada informação do produto.

# 2 - Poderíamos utilizar uma Tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('Good of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teriamos que saber qual é o índice de cada informação do produto.

# 3 - Poderíamos utilizar um Dicionário para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade':  1, 'preco':  2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade':  1, 'preco':  150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação.

# Métodos de dicionários.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)

d.clear()

print(d)

# Copiando um dicionário para outro

# Forma 1 # Deep Copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 # Shallow Copy

novo = d

print(novo)
novo['d'] = 4

print(d)
print(novo)

# Forma não usual de criação de dicionário

"""
a = chave
b = valor
"""
outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um interável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta  chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)

