from time import sleep
def lis():
    print('='*30)


def contador(i, f, p):
    lis()
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if p == 0:
        p = 1
    if i < f:
        for cont in range(i, f + 1, p):
            print(cont, end=' ')
            sleep(0.3)
    elif i > f:
        if p < 0:
            p *= -1
        for cont in range(i, f - 1, -p):
            print(cont, end=' ')
            sleep(0.3)
    if p < 0:
        print(f'Não é possivel contar de {i} até {f} com um passo negativo {p}.')
    else:
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
lis()
print('Agora é sua vez de personalizar a contagem')
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))
lis()
