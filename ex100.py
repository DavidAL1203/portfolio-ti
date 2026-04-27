from time import sleep
from random import randint
numeros = []
def sorteio():
    print('Sorteando 5 valores: ', end='')
    for c in range(0, 5):
        num = randint(1, 10)
        print(f'{num} ', end='')
        sleep(0.5)
        numeros.append(num)
    print('FIM!')
    sleep(0.5)
def somapar():
    soma = 0
    listapar = []
    for n in numeros:
        if n % 2 == 0:
            soma += n
            listapar.append(n)
    if len(listapar) == 0:
        print('Não tem nenhum valor par na lista!')
    else:
        print(f'Os valores par da lista são {listapar} e a soma deles é {soma}')
sorteio()
somapar()
