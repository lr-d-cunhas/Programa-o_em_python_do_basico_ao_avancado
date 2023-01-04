

def multiplicar(num1: float, num2: float) -> float:
    return num1 * num2

resultado: float = multiplicar(4.23434, 6.4343)

print(f'O resultado é {resultado}')

# .2f duas casas decimais
print(f'O resultado é {multiplicar(8, 2):.2f}')

# Colocar entre parêntese (:=)
print(f'{(media := 8 / 2)} é a metade de {media * 2}')

geek: str = 'Rian'

print(f"Rian='{geek}'")

# forma mais simples, -> colocar o sinal de igual no final da variável
print(f'{geek=}')

# Você consegue ver o que está acontecendo.
print(f'{geek.upper()[::-1] = }')


