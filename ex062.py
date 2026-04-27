primeirot = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 1
quantidade = 0
sair = 1
print('Os 10 primeiros termos da PA sao: ', end='')
while contador != quantidade:
    if quantidade == 0:
        quantidade = 11
    pa = primeirot + (contador - 1) * razao
    contador += 1
    if contador == quantidade:
        print('{}.'.format(pa))
        if sair == 2:
            contador = 0
            quantidade = 0
        elif sair == 1:
            print('Você quer ver mais termos dessa PA?')
            sn = int(input('[1]SIM / [2]NÃO\n '))
            if sn == 1:
                quantidade += int(input('Digite quantos termos a mais você quer ver: '))
                sair = 1
            elif sn == 2:
                sair = 2
    else:
        print(pa, end=', ')
print('A progressão foi encerrada com {} termos mostrados!'.format(quantidade - 1))
print('\033[31mSaindo...')
