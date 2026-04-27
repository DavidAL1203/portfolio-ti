print('Os números pares no intervalo entre 1 e 50 são:')
for c in range(2, 51, 2):
    if c != 50:
        print(c, end=', ')
    elif c == 50:
        print('{}.'.format(c))
