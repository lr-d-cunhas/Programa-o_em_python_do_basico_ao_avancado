"""
Unittest - Antes e após hooks


----
hooks - são os testes em si. Ou seja, a execução dos testes.
----


setup() -> é executado antes de cada método de teste. é util para criarmos instâncias de objetos e otros dados;

tearDown() -> é executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com banco de dados.


"""

import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configuração do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vair rodar após o teste.
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown() vair rodar após o teste.
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass

    

