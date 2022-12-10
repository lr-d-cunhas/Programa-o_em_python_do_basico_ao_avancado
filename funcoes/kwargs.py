"""
**Kwargs

Poderíamos chamar este parâmetro de **xix, mas por convenção chamams de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parâmetros  nomeados, e transforma esses
parâmetros extras em um dicionário.
"""

# Exemplo


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é  {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()

cores_favoritas(geek='navy')

# Exemplo mais complexo


def cumprimento_espeial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'Geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return'Não  tenho certeza quem você é ...'


print(cumprimento_espeial())
print(cumprimento_espeial(geek='Python'))
print(cumprimento_espeial(geek='Oi'))
print(cumprimento_espeial(geek='especial'))

"""
# Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs
"""

"""
# Ordem dos parâmetros
1° Parâmetros obrigatórios;
2° *args;
3° Parâmetros default (não obrigatórios);
4° **kwargs
"""


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'julia')
minha_funcao(18, 'Felicity', 4, 5, 3, soletiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 3, 3, java=False, python=True)

# Outro exemplo


def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"seu nome é {kwargs['nome']} e seu sobrenome é {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

# print(mostra_nomes(nomes='Felicity', sobrenome='Jones'))

print(mostra_nomes(**nomes))


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]

soma_multiplos_numeros(*lista)

# OBS! Os nomes da chave em  um dicionário devem ser o mesmo dos parâmetros da função

# dicionario = dict(a=1, b=2, f=3)  # TypeError

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

soma_multiplos_numeros(**dicionario)





