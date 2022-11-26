"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string Tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas
- Aspas duplas tiplas;

Exemplo:
- Aspas simples -> 'Rian'
- Aspas duplas -> "Rian"
- Aspas simples triplas -> ''' Rian '''
"""
# - Aspas duplas triplas -> # """ Rian """

# Entrada de dados
# print('Qual seu nome?')
# nome = input() # input -> Entrada
nome = input('Qual o seu nome ')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a)' %s % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vind(a) {0}'.format(nome))

# Exeplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')


# print('Qual sua idade? ')
# idade = input()
# idade = input('Qual sua idade ')
idade = int(input('Qual sua idade? '))

# Processamento

# Saída de dados
# Exemplo de print 'antigo' 2.x
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('A {0} tem {1} anos'.format(nome, idade))
print(f'O {nome} tem {idade} anos')

"""
# int(idade) => cast 

Cas é a 'conversão' de um tipo de dado para outro.
"""
print(f'O {nome} nasceu em {2022 - idade}')

