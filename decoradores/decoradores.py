"""
Decoradores (Decprators)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Sytact Sugar / Açucar Sintático)

|------------------------------------------------------|
|               Function Decorator                     |
|------------------------------------------------------|

|------------------------------------------------------|
||----------------------------------------------------||
||                   Função decorada                  ||
||----------------------------------------------------||
|------------------------------------------------------|

"""

# Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)


def seja_educado(funcao):
    def sendo():
        print('Foi um  prazer conhecer você|')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():  # Função comum
    print('Seja bem-vindo(a) à Geek University')

# Testando 1

# saudacao()

# teste = seja_educado(saudacao)  # Função decorada

# teste()

# Testanndo 2


def raiva():
    print('EU TE ODEIO!')


# raiva_educada = seja_educado(raiva)

# raiva_educada()

# Decorators com Syntax Sugar (Açúcar Sintático)


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentado():
    print('Meu nome é Pedro')

# Testando
apresentado()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')

# dormir()

"""
---------------------------------------------------------------------
|   Home    |   Serivços    |   Produtos    |   Administrativo      |
---------------------------------------------------------------------

http://www.suaempresa.com.br/home

http://www.suaempresa.com.br/servicos

http://www.suaemresa.com.br/produtos

htt´://www.suaempresa.com.br/admin

# OBS: Não é código funcional (Que funcione) é apenas exemplo


def checa_login(request):
    if not request.usuario:
        redirect('http://www.suaempresa.com.br')


def home(request):
    return 'Pode acessar home'


@checa_login
def servicos(request):
    return 'Pode acessar serviços'


def produtos(request):
    return 'Pode acessar produtos'


@checa_login
def admin(request):
    return 'Pode acessar admin'
        
"""

# OBS: Não confunda Decorator com Decorator Function

