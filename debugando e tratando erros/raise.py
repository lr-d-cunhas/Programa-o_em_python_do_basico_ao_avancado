"""
Levantando os próprios erros com raise

raise -> Lnança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra
em Python.

Para simplificar, pense no raise como sendo útilo para que possamos criar nossas próprias
exceções e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')
"""

# Exemplo real


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'azul')

# Outro exemplo


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser  uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek University', 'Preto')

"""
OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após
o raize é executado
"""




