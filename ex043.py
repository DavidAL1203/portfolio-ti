from time import sleep
print('\033[36m=\033[m'*45)
print('\033[36mCALCULADORA DE ÍNDICE DE MASSA CORPORAL (IMC)\033[m')
print('\033[36m=\033[m'*45)
print('\033[36mTABELA DO IMC:\033[m')
print('\033[36mMENOS DE 18.5: ABAIXO DO PESO\033[m')
print('\033[36mDE 18.5 ATÉ 25: PESO IDEAL\033[m')
print('\033[36mDE 25 ATÉ 30: SOBREPESO\033[m')
print('\033[36mDE 30 ATÉ 40: OBESIDADE\033[m')
print('\033[36mACIMA DE 40: OBESIDADE MÓRBIDA')
print('\033[36m=\033[m'*31)
peso = float(input('\033[34mDigite o seu peso (kg): '))
altura = float(input('\033[34mDigite sua altura (m): '))
print('\033[34mCALCULANDO SEU IMC...\033[m')
sleep(2)
imc = peso / (altura * altura)
if imc < 18.5:
    print('\033[33mVOCÊ ESTÁ ABAIXO DO PESO! SEU IMC É {:.1f}!'.format(imc))
elif 25 > imc >= 18.5:
    print('\033[32mVOCÊ ESTÁ NO PESO IDEAL! SEU IMC É {:.1f}!'.format(imc))
elif 30 > imc >= 25:
    print('\033[33mVOCÊ ESTÁ COM SOBREPESO! SEU IMC É {:.1f}! '.format(imc))
elif 40 > imc >= 30:
    print('\033[31mVOCÊ ESTÁ COM OBESIDADE! SEU IMC É {:.1f}!'.format(imc))
elif imc >= 40:
    print('\033[31mVOCÊ ESTÁ COM OBESIDADE MÓRBIDA! SEU IMC É {:.1f}!'.format(imc))
