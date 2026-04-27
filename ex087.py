#CODIGO REDUZIDO
par = mai = 0
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        lista[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if lista[linha][coluna] % 2 == 0:
            par += lista[linha][coluna]
        if lista[1][coluna] > mai:
            mai = lista[1][coluna]
soma3 = lista[0][2] + lista[1][2] + lista[2][2]
print('-='*20)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{lista[linha][coluna]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {mai}')

#MEU CODIGO ORIGINAL KKKKKKKKKKK
lista = [[], [], []]
somapar = 0
somacoluna3 = 0
maior = 0
for c in range(0, 3):
    n = int(input(f'Digite um valor para [0, {c}]:'))
    lista[0].append(n)
    if n % 2 == 0:
        somapar += n
    if c == 2:
        somacoluna3 += n
for c1 in range(0, 3):
    n = int(input(f'Digite um valor para [1, {c1}]:'))
    lista[1].append(n)
    if n % 2 == 0:
        somapar += n
    if c1 == 2:
        somacoluna3 += n
    if n > maior:
        maior = n
for c2 in range(0, 3):
    n = int(input(f'Digite um valor para [2, {c2}]:'))
    lista[2].append(n)
    if n % 2 == 0:
        somapar += n
    if c2 == 2:
        somacoluna3 += n
print('-='*30)
print(f'[{lista[0][0]:^5}] [{lista[0][1]:^5}] [{lista[0][2]:^5}]')
print(f'[{lista[1][0]:^5}] [{lista[1][1]:^5}] [{lista[1][2]:^5}]')
print(f'[{lista[2][0]:^5}] [{lista[2][1]:^5}] [{lista[2][2]:^5}]')
print('-='*30)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somacoluna3}')
print(f'O maior valor da segunda linha é {maior}')