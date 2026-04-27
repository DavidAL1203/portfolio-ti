from datetime import date
ano = int(input('Digite o ano de nascimento: '))
data = date.today()
idade = data.year - ano

if idade > 18:
    print('\033[31m='*17,'ATENÇÃO!','='*17)
    print('\033[31mJa se passou {} anos do prazo de alistamento!'.format(idade - 18))
    print('\033[31m='*17,'ATENÇÃO!','='*17)
elif idade < 18:
    print('\033[36m='*29)
    print('Você deve se alistar em {}!'.format((18 - idade)+data.year))
    print('\033[36m=' * 29)
elif idade == 18:
    print('\033[33m=' * 54)
    print('É hora de se alistar! Cuidado para não perder o prazo!')
    print('\033[33m=' * 54)
