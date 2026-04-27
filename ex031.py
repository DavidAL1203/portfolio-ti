km = float(input('Digite a distancia da viagem em KM: '))
if 200 >= km > 0:
    print('O preço da viagem de {}km é R${:.2f}.'.format(km, km*0.50))
if km > 200:
    print('O preço da viagem de {}km é R${:.2f}.'.format(km, km*0.45))
if km <= 0:
    print('Digite uma distancia valida.')
