from datetime import date
date = date.today().year
imaior = 0
imenor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    if date - ano >= 21:
        imaior += 1
    else:
        imenor += 1
print('{} pessoas ainda não aingiram a maioridade e {} pessoas ja são maiores de 21 anos!'.format(imenor, imaior))
