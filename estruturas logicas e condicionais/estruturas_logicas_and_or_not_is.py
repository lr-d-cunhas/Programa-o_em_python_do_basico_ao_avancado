"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - no
Operadores binários:
    - and, or, is

Regras de funcionamento:

Pra o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True

"""
ativo = True
logado = False

# Se não estiver ativo
if not ativo:
    print('Você precisa ativar a conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')

# vai ser sempre o contrario
print(not False)

# ativo é Falso
print(ativo is True)

# 1 is 1
# nome is 1
