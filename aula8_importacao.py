#importacao de classes e metodos

from aula7_televisao import Televisao #importa classe Televisao
from aula7_calculadora1 import Calculadora #importa classe calculadora1
from aula8_contador_letras import contador_letras, teste #importa os metodos contador_letras e teste


if __name__ == '__main__':

    televisao = Televisao()

    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calc = Calculadora(5,1)
    print(calc.soma())
    lista = ['cachorro', 'gato', 'elefante']
    print(contador_letras(lista))
    print(teste())