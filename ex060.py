print('\033[34mFATORIAL USANDO WHILE')
n = int(input('Digite um numero: '))
n1 = n
c = n - 1
negativo = 0
if n < 0:
    print('\033[31mNão existe fatorial de números negativos!\033[m')
    negativo = 1
elif n == 0:
    n = 1
    n1 = 0
else:
    while c != 0:
        n *= c
        c -= 1
if negativo == 0:
    print('O fatorial de {} é {}'.format(n1, n))
print('\n')

#==================================================#

print('\033[32mFATORIAL USANDO FOR')
f = int(input('Digite um numero: '))
f1 = f
negativo1 = 0
if f < 0:
    print('\033[31mNão existe fatorial de números negativos!\033[m')
    negativo1 = 1
else:
    if f == 0:
        f1 = 0
        f = 1
    else:
        for i in range(f, 1, -1):
            f *= (i - 1)
    print('O fatorial de {} é {}'.format(f1, f))
