from random import randint
tupla = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Os valores sorteados foram: {tupla[0]} {tupla[1]} {tupla[2]} {tupla[3]} {tupla[4]}')
print(f'O maior valor sorteado foi: {max(tupla)}')
print(f'O menor valor sorteado foi: {min(tupla)}')
