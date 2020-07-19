#definindo uma classe em python

#desta forma a classe deve receber os valores ao ser estanciada
class Calculadora: #por convencao classes comecam com letra maiuscula
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    #definindo metodos em python
    def soma(self):  #metodos com letra minuscula
        return self.valor_a + self.valor_b

    def subtracao (self):
        return self.valor_a - self.valor_b

    def multiplicacao (self):
        return self.valor_a * self.valor_b

    def divisao (self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print(calculadora.valor_b)
    print(calculadora.soma())
    print(calculadora.divisao())
