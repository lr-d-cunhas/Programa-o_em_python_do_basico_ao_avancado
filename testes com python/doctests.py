"""
Doctests

    #>>> soma(1, 2)
    #3

Teste que vai dentro da sua documentação

Doctest são testes que colocamos na docstring das funções/métodos Python.

Para rodar um test do doctest:

Python -m doctest -v nome_do_modulo.py

# Saída
"""

def soma(a, b):
    """Soma os números a e b

    >>> soma(1, 2)
    3

    >>> soma(4, 6)
    10
    """
    return a + b


print(soma(3, 4))  # 7

# Outro Exemplo, Aplicando o TDD

def duplicar(valores):
    """duplica os valores em uma lista

    >>> duplicar([1, 2,  3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsuported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]

# Erro inesperado...

# OBS: Dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.

def fala_oi():
    """Fala oi

    >>> fala_oi()
    'oi'
    """
    return "oi"

# Um último caso estranho...

# Com 2 espaços após o True o teste não passa
def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True
