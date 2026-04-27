salario = float(input('Digite o valor do salário: '))
if salario > 1250:
    print('\033[32mO valor do salário que era R${:.2f} com 10% de aumento ficou R${:.2f}.\033[m'.format(salario, salario+(salario*10/100)))
if 1250 >= salario > 0:
    print('\033[36mO valor do salário que era R${:.2f} com 15% de aumento ficou R${:.2f}.\033[m'.format(salario, salario+(salario*15/100)))
if salario <= 0:
    print('\033[31mDigite um salário valido.\033[m')
