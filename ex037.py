n = int(input('DIGITE UM NUMERO INTEIRO: '))
bc = int(input('Escolha a base de conversão digitando o numero correspondente: \n'
               '1 - Binario\n'
               '2 - Octal\n'
               '3 - Hexadecimal\n'))
bin = bin(n)[2:]
oct = oct(n)[2:]
hex = hex(n)[2:]
if bc == 1:
    print('O binario de {} é {}.'.format(n, bin))
elif bc == 2:
    print('O octal de {} é {}.'.format(n, oct))
elif bc == 3:
    print('o hexadecimal de {} é {}.'.format(n, hex))
else:
    print('O valor digitado é invalido.')
