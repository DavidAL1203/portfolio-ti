n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#NUMERO MAIOR
if n1 > n2 != n3 and n1 > n3:
    print('O número {} é o maior'.format(n1))
if n2 > n1 != n3 and n2 > n3:
    print('O número {} é o maior'.format(n2))
if n3 > n1 != n2 and n3 > n2:
    print('O número {} é o maior'.format(n3))

#NUMERO MENOR
if n1 < n2 != n3 and n1 < n3:
    print('O número {} é o menor'.format(n1))
if n2 < n1 != n3 and n2 < n3:
    print('O número {} é o menor'.format(n2))
if n3 < n1 != n2 and n3 < n2:
    print('O número {} é o menor'.format(n3))

#NUMEROS IGUAIS MAIORES
if n1 == n2 and n1 == n3:
    print('Os três números são iguais: {}'.format(n1))
if n1 == n2 and n1 != n3 and n1 > n3:
    print('Os dois primeiros números são iguais: {}. E maiores que o terceiro numero: {}'.format(n1, n3))
if n1 == n3 and n1 != n2 and n1 > n2:
    print('O primeiro e o terceiro número são iguais: {}. E maiores que o segundo numero: {}'.format(n1, n2))
if n2 == n3 and n2 != n1 and n2 > n1:
    print('O segundo e o terceiro número são iguais: {}. E maiores que o primeiro numero: {}'.format(n2, n1))

#NUMEROS IGUAIS MENORES
if n1 == n2 and n1 != n3 and n1 < n3:
    print('Os dois primeiros números são iguais: {}. E menores que o terceiro número: {}'.format(n1, n3))
if n1 == n3 and n1 != n2 and n1 < n2:
    print('O primeiro e o terceiro número são iguais: {}. E menores que o segundo número: {}'.format(n1, n2))
if n2 == n3 and n2 != n1 and n2 < n1:
    print('O segundo e o terceiro número são iguais: {}. E menores que o primeiro número: {}'.format(n2, n1))
