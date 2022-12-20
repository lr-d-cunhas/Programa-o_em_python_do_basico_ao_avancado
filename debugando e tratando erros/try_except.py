"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.
Previnindo assim que o programa  para de funcionar e o usuário receba mensagens
de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve  ser feito em caso de problema

"""

# Exemplo 1 - Tratando um erro genérico
# Qualquer tipo de erro
try:
    geek()
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erro, imprima a mensagem de erro.

# Outro exemplo

try:
    len(5)
except:
    print('Deu algum problema')

"""
Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é sempre
tratar de forma expecífica.
"""

# Exemplo 3 - Tratando um erro específico

try:
    geek()
except NameError:  # Se der qualquer outro tipo de erro eu não consigo tratar.
    print('Você está utilizando uma função inexistente')

# Exemplo 4 - Tratando um erro específico com detalhes do erro
print()

try:
    len(5)
except TypeError as err:  # Tenta capturar uma exeção do tipo TypeError e chame ela de err
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diferentes tipos de erros

try:
    #len(5)
    geek()
    #print('Geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')


print()
def pega_valor(dicionario, chave):
    try:  # Tenta fazer isso
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'nome': 'Geek'}

print(pega_valor(7, 'game'))

