from random import randint
from time import sleep
print('\033[34m|{}|'.format('='*29))
print('\033[34m|           JOKENPÔ           |')
maquina = randint(1, 3)
jogador = int(input('\033[34m|1 PEDRA | 2 PAPEL | 3 TESOURA|\n'
                    '|{}|\n'
                    ' ESCOLHA UMA OPÇÃO PARA JOGAR:'.format('='*29)))
#EMPATE
if jogador != 1 and jogador != 2 and jogador != 3:
    print('\033[31mOPÇÃO INVALIDA!')
else:
    print('\033[31mJO')
    sleep(0.5)
    print('\033[33mKEN')
    sleep(0.5)
    print('\033[36mPÔ!!!')
    sleep(0.5)
if jogador == maquina:
    print('\033[33m=============EMPATE!=============')
    if jogador == 1 and maquina == 1:
        print('\033[33mJOGADOR (PEDRA) X (PEDRA) MAQUINA')
    elif jogador == 2 and maquina == 2:
        print('\033[33mJOGADOR (PAPEL) X (PAPEL) MAQUINA')
    elif jogador == 3 and maquina == 3:
        print('\033[33mJOGADOR (TESOURA) X (TESOURA) MAQUINA')
    print('\033[33m=============EMPATE!=============')
#JOGADOR VENCE
elif jogador == 1 and maquina == 3 or jogador == 2 and maquina == 1 or jogador == 3 and maquina == 2:
    print('\033[32m============VOCÊ VENCEU!============')
    if jogador == 1 and maquina == 3:
        print('\033[32mJOGADOR (PEDRA) X (TESOURA) MAQUINA')
    elif jogador == 2 and maquina == 1:
        print('\033[32mJOGADOR (PAPEL) X (PEDRA) MAQUINA')
    elif jogador == 3 and maquina == 2:
        print('\033[32mJOGADOR (TESOURA) X (PAPEL) MAQUINA')
    print('\033[32m============VOCÊ VENCEU!============')
#JOGADOR PERDE
elif jogador == 1 and maquina == 2 or jogador == 2 and maquina == 3 or jogador == 3 and maquina == 1:
    print('\033[31m===========VOCÊ PERDEU!===========')
    if jogador == 1 and maquina == 2:
        print('\033[31mJOGADOR (PEDRA) X (PAPEL) MAQUINA')
    elif jogador == 2 and maquina == 3:
        print('\033[31mJOGADOR (PAPEL) X (TESOURA) MAQUINA')
    elif jogador == 3 and maquina == 1:
        print('\033[31mJOGADOR (TESOURA) X (PEDRA) MAQUINA')
    print('\033[31m===========VOCÊ PERDEU!===========')
