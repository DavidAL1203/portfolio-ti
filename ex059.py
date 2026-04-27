from time import sleep
op = 0
n1 = 0
n2 = 0
ok = 0
reiniciar = 0
while op != 5:
    if op == 0:
        if ok != 2:
            n = int(input('\033[33mDigite um numero: '))
            if n1 != n and ok == 0:
                n1 = n
            if n2 != n and ok == 1:
                n2 = n
            ok += 1
        if ok == 2:
            print('\033[36m='*3, 'ESCOLHA UMA OPÇÃO', '='*3)
            print('\033[33m[1]\033[34mSomar\n'
                  '\033[33m[2]\033[34mMultiplicar\n'
                  '\033[33m[3]\033[34mMaior\n'
                  '\033[33m[4]\033[34mNovos Números\n'
                  '\033[33m[5]\033[34mSair do Programa')
            op = int(input(' '))
            if op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
                op = 0
                print('\033[31mOPÇÃO INVALIDA!')
            if op == 1:
                print('\033[33mA soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
                sleep(2)
                print('\033[36m='*3, 'ESCOLHA UMA OPÇÃO', '='*3)
                while reiniciar != 1:
                    reiniciar = int(input('\033[33m[1]\033[34mREINICIAR\n'
                                          '\033[33m[2]\033[34mSAIR\n'
                                          '\033[36mDeseja reiniciar ou sair?\n'
                                          ''))
                    if reiniciar == 1:
                        op = 0
                        ok = 0
                        print('\033[35mREINICIANDO...')
                    if reiniciar == 2:
                        op = 5
                        reiniciar = 1
                    if reiniciar != 1 and reiniciar != 2:
                        print('\033[31mOPÇÃO INVALIDA!')
            if op == 2:
                print('\033[33mA multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
                sleep(2)
                print('\033[36m=' * 3, 'ESCOLHA UMA OPÇÃO', '=' * 3)
                while reiniciar != 1:
                    reiniciar = int(input('\033[33m[1]\033[34mREINICIAR\n'
                                          '\033[33m[2]\033[34mSAIR\n'
                                          '\033[36mDeseja reiniciar ou sair?\n'
                                          ''))
                    if reiniciar == 1:
                        op = 0
                        ok = 0
                        print('\033[35mREINICIANDO...')
                    if reiniciar == 2:
                        op = 5
                        reiniciar = 1
                    if reiniciar != 1 and reiniciar != 2:
                        print('\033[31mOPÇÃO INVALIDA!')
            if op == 3:
                if n1 > n2:
                    maior = n1
                elif n1 < n2:
                    maior = n2
                else:
                    maior = n1
                if n1 != n2:
                    print('\033[33mO maior número digitado foi {}'.format(maior))
                elif n1 == n2:
                    print('\033[33mOs dois números são iguais {}'.format(maior))
                sleep(2)
                while reiniciar != 1:
                    reiniciar = int(input('\033[33m[1]\033[34mREINICIAR\n'
                                          '\033[33m[2]\033[34mSAIR\n'
                                          '\033[36mDeseja reiniciar ou sair?\n'
                                          ''))
                    if reiniciar == 1:
                        op = 0
                        ok = 0
                        print('\033[35mREINICIANDO...')
                    if reiniciar == 2:
                        op = 5
                        reiniciar = 1
                    if reiniciar != 1 and reiniciar != 2:
                        print('\033[31mOPÇÃO INVALIDA!')
            if op == 4:
                op = 0
                ok = 0
                print('\033[35mREINICIANDO...')
            sleep(1)
    reiniciar = 0
print('\033[31mSAINDO...')
sleep(2)
