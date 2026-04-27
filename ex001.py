import random
limpar = '\033[m'
cor = random.randint(1,8)
if 1 == cor:
    cor = '\033[30m'
if 2 == cor:
    cor = '\033[31m'
if 3 == cor:
    cor = '\033[32m'
if 4 == cor:
    cor = '\033[33m'
if 5 == cor:
    cor = '\033[34m'
if 6 == cor:
    cor = '\033[35m'
if 7 == cor:
    cor = '\033[36m'
if 8 == cor:
        cor = '\033[37m'
print('{}Olá Mundo!{}'.format(cor, limpar))
