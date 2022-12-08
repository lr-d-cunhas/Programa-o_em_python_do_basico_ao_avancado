"""
Funções com Parâmetro Padrão (Default Parametros)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')

print()

# Exemplo de função onde a passgame de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado())  # TypeError

"""

# Quando coloca "potencia=2" esse padrão ele se torna opcional


def exponencial(numero, potencial=2):
    return numero ** potencial


print(exponencial(2, 3))  # 2 * 2 * 2
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))  # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva á potência informada pelo usuário

# OBS
# Se o usuário passar somente 1 parâmetro, este será atribuído ao parâmetro numero, e será calculado o quadrado deste número:
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro numero e o segundo ao parâmetro potencia. Enão
# Será calculada esta potência.

# print(exponencial())

# OBS: Em função Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração

# ERRO!
"""
def teste(num=2, potencia):
    return num ** potencia
"""

# Outros exemplos


def soma(num1=5, num2=3):
    return num1 + num2


print(soma(4, 3))
print(soma(4))
print(soma())


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))

# Por quê utilizar parâmetros com valor default?
"""
- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;
- Podemos uzar qualquer tipo de dados como parâmetros

"""

# Quais tipos de dados podemos utilizar com valores default para parâmetros?

# Exemplos


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas de confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # Variável global


def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'Oi {instrutor}'


print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência


def diz_oi():
    prof = 'Geek'  # Variável local
    return f'Olá {prof}'


print(diz_oi())

# print(prof) # NameError

# ATENÇÃO com variáveis globais (Se puder evitar, evite!)

total = 0

"""
def incrementa():
    total = total + 1  # UnboundLocalError (A variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total


print(incrementa())
"""

total = 0


def incrementa():  # Avisando que queremos utilizar a variável global
    global total
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())

"""
OBS: Variável local tera preferência
"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # Não é local, ela é uma não local, mas não é global, elas está em uma função anterior
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())
