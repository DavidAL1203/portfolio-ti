idades = 0
ivelho = 0
hv = str
mulheres = 0
pessoas = 0
for c in range(1, 5):
    nome = input('Digite o nome:').strip().title()
    idade = int(input('Digite a idade:'))
    sexo = str(input('Digite o sexo (M/F):').strip().upper())
    print('-'*25)
    idades += idade
    if sexo == 'M' or sexo == 'F':
        pessoas += 1
    if sexo == 'M':
        if idade > ivelho:
            ivelho = idade
            hv = nome
    if sexo == 'F':
        if idade < 20:
            mulheres += 1
media = idades / 4
if pessoas == 4:
    print('A média de idade do grupo é {} anos.'.format(media))
    print('O homem mais velho é {} e ele tem {} anos.'.format(hv, ivelho))
    print('Tem {} mulheres com menos de 20 anos.'.format(mulheres))
else:
    print('Você digitou algum dado errado!')
