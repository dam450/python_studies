#lambda - criando funções anônimas (ideal para funções
# com codigo que se resolvam em 1 linha

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(subtracao(5,10))

#dicionario de funcoes lambda
# <class 'dict'>
calculadora = {
    'soma': lambda  a, b: a + b,
    'subtracao': lambda  a, b: a - b,
    'multiplicacao': lambda  a, b: a * b,
    'divisao': lambda  a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma'] # soma = lambda  a, b: a + b
multiplicacao = calculadora['multiplicacao']

print('a soma é: {}' .format(soma(10, 5)))
print('a multiplição é: {}' .format(multiplicacao(10, 5)))