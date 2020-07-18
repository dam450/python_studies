# for x in range(1, 101):
#     print(x)

# a = int(input("entre com um número:"))
#
# div = 0
#
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div+=1
#
# if div == 2 :
#     print('número {} é primo' .format(a))
# else:
#     print('número {} não é primo'.format(a))


# for num in range(101):
#     div = 0
#     for x in range(1, num + 1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)

#
# a = int(input('Primeiro Bimestre: '))
# while a > 10:
#     a = int(input('Valor Inválido! \n\nPrimeiro Bimestre: '))
#
# b = int(input('Segundo Bimestre: '))
# while b > 10:
#     b = int(input('Valor Inválido! \n\nSegundo Bimestre: '))
#
# c = int(input('Terceiro Bimestre: '))
# while c > 10:
#     c = int(input('Valor Inválido! \n\nTerceiro Bimestre: '))
#
# d = int(input('Quarto Bimestre: '))
# while d > 10:
#     d = int(input('Valor Inválido! \n\nQuarto Bimestre: '))
#
# media = (a + b + c + d) / 4
#
# print('média igual a {}' .format(media))

resultado = 0
for x in range(1, 10):
    if x < 9:
        resultado += 1
print(resultado)