"""
int, str, float, List, Set, Dict, etc
"""


def dobro(valor: int) -> int:
    return valor * 2


print(dobro(8))

# É preferivel que seja inteiro o valor informado
# mas não ira impedir que a função funcione
# mas isso será questionado no mypy
print(dobro('Geek'))

"""
- Literal type
- Union
- Typed dictionaries
- Protocols
"""

# Literal type

from typing import Literal

# Estamos informando saídas específica
def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass

def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        # !r -> Coloca o valor entre aspas ''
        raise ValueError(f'Operação inválida {operacao!r}')

# Refatorando
# ao executar com mypy ele acusa um erro
def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        # !r -> Coloca o valor entre aspas ''
        raise ValueError(f'Operação inválida {operacao!r}')


calcula_v2('+', 6, 4)
calcula_v2('-', 10, 2)
# calcula_v2('*', 3, 5)

# Union
from typing import Union

def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande.'
    else:
        return resultado


# Final

"""
Criar constantes
"""
from typing import Final

NOME: Final = 'Rian'

print(NOME)

NOME = 'Rian'

print(NOME)

from typing import final

@final
class Pessoa:
    pass

class Estudante(Pessoa):
    pass

    @final
    def estudar(self):
        print('Estou estudando...')

class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Estudando e estagiando...')


# Typed Dictionaries

from typing import TypedDict

# Dicionário tipado
class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.8.5', atualizacao=2020)

print(geek)

outro = CursoPython(algo='vai', coisa=True)

print(outro)

# Protocols

"""
Definimos que os objetos que seguirem esse protocolo vão ter um atributo titulo
"""

from typing import Protocol


class Curso(Protocol):
    titulo: str

    def __init__(self):
        Curso.titulo = 'Programação em Python'


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = 'Oi'

v1 = Venda()
c1 = Curso()

estudar(c1)
estudar(v1)
