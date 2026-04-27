def calculadora(op, num1, num2, resultado):
    if op == 1:
        resultado = num1 + num2
    elif op == 2:
        resultado = num1 - num2
    elif op == 3:
        resultado = num1 * num2
    elif op == 4:
        resultado = num1 / num2
    print(f'Resultado: {resultado}')


while True:
    print(f'==========-CALCULADORA-==========')
    opcao = (int(input('1 - SOMA \n'
                          '2 - SUBTRAÇÃO \n'
                          '3 - MULTIPLIÇÃO \n'
                          '4 - DIVISÃO \n'
                          '0 - SAIR \n'
                          '================================= \n'
                          'Escolha uma operação: ')))
    if opcao != 0:
        if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
            n1 = (float(input(f'Digite o primeiro número: ')))
            n2 = (float(input(f'Digite o segundo número: ')))
            calculadora(opcao, n1, n2, 0)
        else:
            print('Opção Invalida.')
    else:
        break
print('Saindo...')
