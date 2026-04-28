historico = []
while True:
  print(f'{'='*10}-CALCULADORA-{'='*10}')
  op = int(input('1 - SOMA \n2 - SUBTRAÇÃO \n3 - MULTIPLICAÇÃO \n4 - DIVISÃO \n5 - HISTÓRICO \n0 - SAIR \nOPERAÇÃO: '))
  if op == 0:
    break
  else:
    if op == 1:
      n1 = float(input('NÚMERO 1: '))
      n2 = float(input('NÚMERO 2: '))
      print(f'{n1} + {n2} = {n1+n2}')
      historico.append(f'{n1} + {n2} = {n1+n2}\n')
    elif op == 2:
      n1 = float(input('NÚMERO 1: '))
      n2 = float(input('NÚMERO 2: '))
      print(f'{n1} - {n2} = {n1-n2}')
      historico.append(f'{n1} - {n2} = {n1-n2}\n')
    elif op == 3:
      n1 = float(input('NÚMERO 1: '))
      n2 = float(input('NÚMERO 2: '))
      print(f'{n1} * {n2} = {n1*n2}')
      historico.append(f'{n1} * {n2} = {n1*n2}\n')
    elif op == 4:
      n1 = float(input('NÚMERO 1: '))
      n2 = float(input('NÚMERO 2: '))
      if n2 == 0:
        print('NÃO É POSSÍVEL DIVIDIR POR ZERO')
      else:
        print(f'{n1} / {n2} = {n1/n2}')
        historico.append(f'{n1} / {n2} = {n1/n2}\n')
    elif op == 5:
      print('='*30)
      for item in historico:
        print(item)
    else:
      print('OPÇÃO INVÁLIDA')
    print('='*30)
print('Saindo...')
