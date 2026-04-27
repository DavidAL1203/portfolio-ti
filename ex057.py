sx = ''
sexo = ''
while sx != 'm' and sx != 'f':
    if sx != 'm' and sx != 'f':
        sx = str(input('\033[33mInforme seu sexo [M/F]: ')).strip().lower()
    if sx != 'm' and sx != 'f':
        print('\033[31mOpção invalida, tente novamente.')
    if sx == 'm':
        sexo = 'Masculino'
    if sx == 'f':
        sexo = 'Feminino'
if sexo == 'Masculino':
    print('\033[34m')
elif sexo == 'Feminino':
    print('\033[35m')
print('Seu sexo é {}!'.format(sexo))
