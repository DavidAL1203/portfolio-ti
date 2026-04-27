c = continuar = op = soma = cont = maior = menor = 0
while c != 1:
    if op == 0:
        n = int(input('Digite um número: '))
        soma += n
        cont += 1
        if n > maior:
            maior = n
        if menor == 0:
            menor = n
        elif n < menor:
            menor = n
    if continuar == 0:
        sn = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if sn == 'S':
            continuar = 0
        elif sn == 'N':
            c = 1
        else:
            print('Opção Invalida!')
            continuar = 0
            op = 1
media = soma / cont
print('A MÉDIA entre os {} números digitados é {}!\n'
      'O MAIOR número digitado foi {}!\n'
      'O MENOR número digitado foi {}!'.format(cont, media, maior, menor))
