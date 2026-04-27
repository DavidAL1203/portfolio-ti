n=input('Digite o nome do funcionario: ')
s=float(input('Digite o salario atual do funcionario: '))
print('O salario de {} que era R${:.2f} fica R${:.2f} com 15% de aumento!'.format(n, s, s+(s*0.15)))
