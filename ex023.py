n = input('Digite um número de 0 a 9999: ')
#print('Número: {}'.format(n))
#print()
#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))
print()

n = int(n)
unidade = n % 10
print('Unidade: {}'.format(unidade))
dezena = n // 10 % 10
print('Dezena: {}'.format(dezena))
centena = n // 100 % 10
print('Centena: {}'.format(centena))
milhar = n // 1000 % 10
print('Milhar: {}'.format(milhar))
