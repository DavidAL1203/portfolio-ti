import math
cato= float(input('Digite o valor do cateto oposto: '))
cata= float(input('Digite o valor do cateto adjacente: '))
hip=math.hypot(cato,cata)
print('A hipotenusa do triangulo retangulo é {:.2f}!'.format(hip))
