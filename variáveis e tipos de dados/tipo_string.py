"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234'''', '''a''', '''True''', '''42.3'''
"""
# - Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "'Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = """Angelina
jolie"""
print(nome)
print(type(nome))

# \" Caracterie de escape
nome = "Angelina \" Jolie"
print(nome)

# maiúsculo
print(nome.upper())

# minusculo
print(nome.lower())

# pega cada palavra e coloca em uma lista
print(nome.split())

print(nome[0:4])  # Slice de string

print(nome[5:15])  # Slice de string

# Pega a primeira palavra da frase
print(nome.split()[0])

# [::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
print(nome.split()[0][::-1])

# Subistitui uma letra por outra dentro da palavra selecionada
print(nome.split()[4].replace('S', 'R'))
