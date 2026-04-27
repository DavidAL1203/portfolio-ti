from random import randint
from time import sleep

n = int(input('Em qual numero de 0 a 5 eu estou pensando? '))
n1 = randint(0,5)
if n == n1:
    print('CARREGANDO...')
    sleep(2)
    print('O número que eu estava pensando era {}. Você ganhou, PARABENS!'.format(n1))
if n != n1:
    print('CARREGANDO...')
    sleep(2)
    print('O número que eu estava pensando era {}. Você perdeu, SINTO MUITO!'.format(n1))
