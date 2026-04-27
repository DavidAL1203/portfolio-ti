casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salario do comprador? '))
anos = int(input('Em quantos anos o comprador vai pagar? '))


if (casa / (anos * 12)) > salario * 30 / 100:
    print('Financiamento negado. Infelizmente o cliente não pode financiar este imovel!')
elif salario * 30 / 100 >= (casa / (anos * 12)):
    print('O valor da parcela mensal do financiamento ficou R${:.2f}.'.format((casa / (anos * 12))))
elif casa<= 0 or salario <= 0 or anos <= 0:
    print('Voce digitou algum dado incorretamente.')
