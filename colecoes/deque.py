"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance
"""

# Importa
from collections import deque

# Criando deques

deq = deque('rian lucas')

print(deq)

# Adicionando elementos no daque

deq.append('y')  # Adiciona no final

print(deq)

deq.appendleft('k')  # Adiciona no começo

print(deq)

# Remover elementos

print(deq.pop())  # Remove e retorna o último elemento

print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento

print(deq)