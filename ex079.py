lista = []
continuar = 'S'
while continuar != 'N':
    valor = (int(input('Digite um valor: ')))
    if valor in lista:
        print('O valor informado ja faz parte da lista.')
    else:
        lista.append(valor)
        print('Valor adicionado!')
    continuar = str(input('Deseja add outro valor? [S/N] ')).upper()
print(f'{'='*35}')
lista.sort()
print(f'Você digitou os valores {lista}')
