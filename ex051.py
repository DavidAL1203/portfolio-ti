a1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão de uma PA: '))
pa = int
print('Os 10 primeiros termos da PA são: ', end='')
for c in range(1, 11):
    pa = a1 + (c - 1) * r
    if c == 10:
        print('{}.'.format(pa))
    else:
        print(pa, end=', ')
