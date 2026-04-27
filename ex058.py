from random import randint
pc = randint(1, 11)
jogador = int
cont = 1
print('De 1 a 10, tente adivinhar em que número o computador esta pensando...')
while pc != jogador:
    jogador = int(input('Em qual numero estou pensando? '))
    if jogador > pc:
        print('Menos... Tente novamente!')
        cont += 1
    elif jogador < pc:
        print('Mais... Tente novamente!')
        cont += 1
if cont == 1:
    print('Muito bem! Você acertou de primeira!\n'
          'O número que eu pensei foi {}.'.format(pc))
elif 5 >= cont > 1:
    print('Parabéns, você acertou em {} tentativas!\n'
          'O número que eu pensei foi {}.'.format(cont, pc))
elif cont > 5:
    print('Você acertou em {} tentativas!\n'
          'O número que eu pensei foi {}.'.format(cont, pc))
