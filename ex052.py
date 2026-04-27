n = int(input('Digite um numero: '))
s = 0
for c in range(1, n + 1):
    if n % c == 0:
        s += 1
if s == 2:
    print('O número {} é primo'.format(n))
else:
    print('O número {} não é primo'.format(n))
