a = int(input("entre com o primeiro valor:"))
b = int(input("entre com o segundo valor:"))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = ('Soma: {val1} + {val2} = {soma} \n'
       'Subtracao: {val1} - {val2} = {subt} \n'
       'Multiplicacao: {val1} x {val2} = {mult} \n'
       'Divisao: {val1} / {val2} = {divi} \n'
       'Resto: {val1} / {val2} sobra {rest}' .format(val1=a,
                                                 val2=b,
                                                 soma=soma,
                                                 subt=subtracao,
                                                 mult=multiplicacao,
                                                 divi=divisao,
                                                 rest=resto))

print(resultado)