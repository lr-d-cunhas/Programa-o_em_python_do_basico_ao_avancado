"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.
"""

"""
# Else -> É executado somente se não ocorrer o erro.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você difitou {num}')

# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não difitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Exectuando o finally')

"""

"""
OBS: O bloco finally é SEMPRE executado. Independente se houve exceção ou não.
O finally, geralmente, é utilizado para fechar ou desalocar recursos. 

"""

# Exemplo mais complexo CORRETO
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!

"""
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        print(f'Valor incorreto')
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'


num1 = input('informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
"""

"""
# Tratamento genérico 

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'


num1 = input('informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

"""

"""
# Exemplo mais complexo - Semi-Genérico
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:  # Eu posso passar mais de um erro que possa ocorrer na mesma linha
        # Eu também posso passar um apelido para ambos os problemas
        return f'Ocorreu um problema: {err}'


num1 = input('informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

"""
