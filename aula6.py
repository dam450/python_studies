#aula de conjuntos (classe do tipo set)

# ctrl + /   ativa/desativa cometarios

# #parte 1
#
# conjunto = {1, 2, 3, 4, 4, 2}  #elementos repetidos são descartados
# print(type(conjunto))
# print(conjunto)
#
# conjunto.add(5)  #metodo adiciona elemento
# conjunto.discard(2) #metodo descarta elemento
#
# print(conjunto)

#parte 2

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2) #metodo gera a uniao dos conjuntos
print(conjunto_uniao)
conjunto_intersect = conjunto.intersection(conjunto2) #metodo gera a intersecçao dos conjuntos  elementos em comum de dois conjuntos
print(conjunto_intersect)
conjunto_diferenca = conjunto.difference(conjunto2) #metodo retorna a diferenca para o 2o conjunto elementos que estão no primeiro conjunto, e não aparecem no segundo
print(conjunto_diferenca)

conjunto_difsim = conjunto.symmetric_difference(conjunto2) #metodo retorna o que esta fora da interseccao dos conjuntos
print(conjunto_difsim)

conjunto_a = {1,2,3,4,5,}
conjunto_b = {2,4,5}
subconjunto = conjunto_b.issubset(conjunto_a) #retorna se um conjunto é um subconjunto de outro (b esta dentro de a)
print(subconjunto)

superconjunto = conjunto_a.issuperset(conjunto_b) #retorna se um conjunto é superconjunto de outro (a contem b)
print(superconjunto)

lista = ['cachorro', 'gato', 'gato', 'elefante', 'cachorro'] #lista com elementos repetidos
conjunto_animais = set(lista) #convertendo a lista em conjunto as duplicidades são eliminadas
print(conjunto_animais)

lista_animais = list(conjunto_animais) #converte o conjunto em listaprint(lista_animais)
conjunto_b.add(7)
conjunto_b.discard(7)
print(conjunto_a.union(conjunto_b))