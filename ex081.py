lista = []
cont = 0
continuar = 's'
while not continuar == 'N':
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    cont += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
print(f'Foram digitados {cont} valores')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
