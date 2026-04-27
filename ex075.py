numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} {'vez' if numeros.count(9) == 1 else 'vezes'}.')
if numeros.count(3) == 0:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
print(f'Os valores pares digitados foram: {numeros[0] if numeros[0] % 2 == 0 else ''} {numeros[1] if numeros[1] % 2 == 0 else ''} {numeros[2] if numeros[2] % 2 == 0 else ''} {numeros[3] if numeros[3] % 2 == 0 else ''}')
