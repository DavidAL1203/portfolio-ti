n = int(input('{}\n'
              'Sequência de Fibonacci\n'
              '{}\n'
              'Quantos termos você quer mostrar? '.format('-'*22, '-'*22))) - 1
print('0')
c = 0
n1 = 1
n2 = 0
n3 = 0
while c != n:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    c += 1
    print('{}'.format(n3))
