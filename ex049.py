n = int(input('Digite um numero para ver a sua tabuada: '))
print('\033[36m='*13)
for c in range(1, 11):
    print('\033[34m{} x {:2} = {}'.format(n, c, n * c))
print('\033[36m='*13)
