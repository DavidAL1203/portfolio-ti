lista = []
listaPAR = []
listaIMPAR = []
continuar = 'S'
while not continuar == 'N':
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
for c in range (0, len(lista)):
    if lista[c] % 2 == 0:
        listaPAR.append(lista[c])
    else:
        listaIMPAR.append(lista[c])
print('='*100)
print(f'A lista completa é {lista}\n'
      f'A lista de pares é {listaPAR}\n'
      f'A lista de ímpares é {listaIMPAR}')
