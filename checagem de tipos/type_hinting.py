"""
você define o tipo de dado que o parâmetro da função recebe
e também especificar o tipo de dado de retorno (-> str:)
"""


def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'


print(cumprimentar('Rian'))


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('Rian Lucas'))

# Saida, para cada caracterie ele colocou um --- em baixo
"""
Rian Lucas
----------
"""

print(cabecalho('Rian Lucas', alinhamento=False))

# Saida
# ####################Rian Lucas####################
# .center(50, '#') -> Centraliza o conteudo, em 50 caracteries, preenchendo as laterais com '#'

print(cabecalho('Rian Lucas', alinhamento='geek'))  # o type_hinting não impede que a função seja executada

