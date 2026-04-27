from random import randint
from time import sleep
lista = []
dados = []
print('='*40)
print(f'{'JOGA NA MEGA SENA':^40}')
print('='*40)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{f' SORTEANDO {jogos} JOGOS ':=^40}')
while jogos > 0:
    for c in range(0, 6):
        n = randint(1, 60)
        while n in dados:
            n = randint(1, 60)
        dados.append(n)
    dados.sort()
    lista.append(dados[:])
    jogos -= 1
    dados.clear()
for c in range(0, len(lista)):
    print(f'jogo {c+1}: {lista[c]}')
    sleep(1)
print(f'{' < BOA SORTE! > ':=^40}')
