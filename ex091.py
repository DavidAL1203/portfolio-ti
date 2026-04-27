from random import randint
from time import sleep
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print(f'========={'RANKING'}=========')
ranking = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)
