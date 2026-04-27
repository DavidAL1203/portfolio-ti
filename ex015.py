d=int(input('Digite a quantidade de dias em que o carro ficou alugado: '))
km=float(input('Digite a quantidade de kilómetros rodados: '))
p=(d*60)+(km*0.15)
print('Considerando o valor de R$60.00 por dia e R$0.15 por km rodado, o valor a ser pago pelo aluguel do carro é de R${:.2f}!'.format(p))
