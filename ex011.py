l=float(input('Largura: '))
a=float(input('Altura: '))
print('Sua parede mede {} x {} e a área da parede é {:.2f}m²!'.format(l, a, l*a))
print('Sera necessario {:.2f} litros de tinta para pintar a parede!'.format((l*a)/2))
