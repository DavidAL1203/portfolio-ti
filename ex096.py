def area(l, c):
    print(f'A área de um terreno {l}x{c} é de {l*c}m².')
print('Controle de terrenos\n'
      f'{'-'*20}')
area(float(input('Largura (m): ')),
     float(input('Comprimento (m): ')))
