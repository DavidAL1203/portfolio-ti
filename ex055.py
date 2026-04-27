maior = 0
menor = 0
for c in range(1, 6):
    p = float(input('Digite o peso da {}º pessoa: '.format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso foi {}kg e o menor peso foi {}kg'.format(maior, menor))
