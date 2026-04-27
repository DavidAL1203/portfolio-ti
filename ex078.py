lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Os valores digitados foram: {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for posicao, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{posicao}', end=' ')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for posicao, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{posicao}', end=' ')
