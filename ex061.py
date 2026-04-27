a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 1
print('Os 10 primeiros termos da PA sao: ', end='')
while c != 11:
    pa = a1 + (c - 1) * r
    c += 1
    if c == 11:
        print('{}.'.format(pa))
    else:
        print(pa, end=', ')
