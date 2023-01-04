"""
É possível fazer o type hinting em forma de comentário, mas não é recomendado!

"""
import math

# Exemplo 1

def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio

print(circunferencia(8))

# Exemplo 2


def cabecalho(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


# cabecalho(texto=43, alinhamento='geek')

# Exemplo 3


def cabecalho2(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


cabecalho(texto='42', alinhamento=False)

nome = 'Rian Lucas'  # type: str


