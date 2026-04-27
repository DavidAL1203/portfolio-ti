nota1 = float(input('\033[34mDigite a primeira nota: \033[m'))
nota2 = float(input('\033[34mDigite a segunda nota: \033[m'))
media = (nota1 + nota2) / 2

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print('\033[31mAs notas são invalidas!\033[m')
else:
    if media < 5:
        print('\033[31mREPROVADO! Sua média foi {}.\033[m'.format(media))
    elif 7 > media >= 5:
        print('\033[33mRECUPERAÇÃO! Sua média foi {}.\033[m'.format(media))
    elif media >= 7:
        print('\033[36mAPROVADO! Sua média foi {}.\033[m'.format(media))
