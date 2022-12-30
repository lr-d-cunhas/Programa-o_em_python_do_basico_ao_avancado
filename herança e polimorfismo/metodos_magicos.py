"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

dunder init -> __init__()

Dunder -> Duble Underscore

dunder repr -> Representação do objeto

dunder str -> Representação do objeto (se tiver o repr, esse terá preferência e aquele será descartado)


"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas  # ou len(self.titulo)

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, outro):
        """self é o primeiro elemento"""
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'

livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)

print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)

print(livro1 * 3)



