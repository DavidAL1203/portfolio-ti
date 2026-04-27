frase = str(input('Digite uma frase: ')).strip().upper().replace(' ','')
inverso = frase[::-1]
if inverso == frase:
    print('O inverso de {} é {}, por isso é palíndromo'.format(frase, inverso))
else:
    print('O inverso de {} é {}, por isso não é palíndromo'.format(frase, inverso))
