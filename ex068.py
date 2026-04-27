from random import randint
pc = cont = record = 0
pi = str
print(f'{'=-'*30}\n'
          f'JOGO PAR OU IMPAR')
while True:
    pc = randint(1, 10)
    print(f'{'=-'*30}')
    n = int(input('Digite um valor: '))
    while pi != 'P' and pi != 'I':
        pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        if pi not in 'PI':
            print('Opção Invalida!')
    resultado = n + pc
    print('-'*60)
#JOGADOR GANHA
    if resultado % 2 == 0 and pi == 'P':
        cont += 1
        print(f'Você jogou {n} e o computador {pc}. O total deu {resultado} que é PAR!')
        print('-' * 60)
        print('VOCÊ VENCEU!\n'
              f'PONTUAÇÃO: {cont}\n'
              'Vamos jogar novamente...')
    elif resultado % 2 != 0 and pi == 'I':
        cont += 1
        print(f'Você jogou {n} e o computador {pc}. O total deu {resultado} que é ÍMPAR!')
        print('-' * 60)
        print('VOCÊ VENCEU!\n'
              f'PONTUAÇÃO: {cont}\n'
              'Vamos jogar novamente...')
#JOGADOR PERDE
    elif resultado % 2 != 0 and pi == 'P':
        print(f'Você jogou {n} e o computador {pc}. O total deu {resultado} que é ÍMPAR!')
        print('-' * 60)
        print('VOCÊ PERDEU!')
        break
    elif resultado % 2 == 0 and pi == 'I':
        print(f'Você jogou {n} e o computador {pc}. O total deu {resultado} que é ÍMPAR!')
        print('-' * 60)
        print('VOCÊ PERDEU!')
        break
    pi = ''
print('=-'*30)
print(f'GAME OVER! Você venceu {cont} vezes.')
