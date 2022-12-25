"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);

OBS: O cocntrarío não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)
-----------------------------------------------------------------------------------
|Funções                                 | Generator Functions                    |
-----------------------------------------------------------------------------------
| utilizam return                        | utilizam yield                         |
-----------------------------------------------------------------------------------
| retornoa uma vez                       | podem utilizar yield múltiplas vezes   |
-----------------------------------------------------------------------------------
| quando executada, retorna um valor     | quanto executada, retorna um generator |
-----------------------------------------------------------------------------------

"""

# Exemplo Função Geradora (Generator Function)


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador  # retornamos o contador mas não saimos da função continuamos dentro dela
        # ao contrario do return
        contador = contador + 1


# OBS: Uma Generator Function não é um Generator. Ela gera um generator. ok?

gen = list(conta_ate(10))

print(gen)

