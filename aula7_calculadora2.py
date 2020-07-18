#definindo uma classe em python

# esta classe recebe valores atraves dos metodos e nao ao estanciar a classe
class Calculadora: #por convencao classes comecam com letra maiuscula
    def __init__(self):
        pass

    #definindo metodos em python
    def soma(self, valor_a, valor_b):  #metodos com letra minuscula
        return valor_a + valor_b

    def subtracao (self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao (self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao (self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()

print(calculadora.soma(10, 4))
print(calculadora.subtracao(10, 3))
print(calculadora.divisao(5, 3))
print(calculadora.multiplicacao(7, 3))
