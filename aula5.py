lista = [9, 3, 5, 7, 8, 2, 16]

lista_ani = ['gato', 'cachorro', 'papagaio', 'macaco', 'arara']

lista_ani.sort() #ordena a lista
print(lista_ani)

lista_ani[1] = 'morcego' #altera valor de uma posicao da lista

lista_ani.reverse() #lista em ordem reversa
print(lista_ani)


#print(lista_ani[2])

soma = 0
for x in lista:
    print(x)
    soma += x

#print('total {}' .format(soma))

#print(sum(lista))

print('mínimo {}' .format(min(lista)))
print('máximo {}' .format(max(lista)))
print('soma {}' .format(sum(lista)))

if 'bode' in lista_ani:
    print('existe um bode na lista')
else:
    print('não tem bode')

lista_ani.append('lobo') #adiciona na lista
print(lista_ani)

lista_ani.pop(1) #pop sem parametro remove ultimo da lista. OBS: 1a posicao da lista é 0

lista_ani.remove('gato') #remove item da lista

print(lista_ani)

#tuplas --- sao imutaveis e criada com conteudo entre parenteses

tupla = (10, 9, 3, 12, 8)
print(tupla)
print(tupla[2])
print(len(tupla)) #retorna quantos elementos tem na lista/tupla

tupla_animal = tuple(lista_ani) #tuple converte a var pro tipo tupla
print(type(tupla_animal)) # type retorna o tipo da var
print(tupla_animal)

lista_numerica = list(tupla) # list converte a tupla em lista e armazena na var
print(type(lista_numerica))
lista.insert()