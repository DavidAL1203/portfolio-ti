import math
a=float(input('Digite um angulo:'))
seno=math.sin(math.radians(a))
cosseno=math.cos(math.radians(a))
tangente=math.tan(math.radians(a))
print('O angulo de {:.2f} tem o seno {:.2f}, cosseno {:.2f} e tangente {:.2f}!'.format(a, seno, cosseno, tangente))
