from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('\033[31m=-='*8)
print('\033[33mANALISANDO SEU NUMERO...')
print('\033[31m=-='*8)
sleep(2)
if n1 > n2:
    print('\033[34mO primeiro valor "{}" é maior que o segundo valor "{}"'.format(n1, n2))
elif n1 < n2:
    print('\033[34mO segundo valor "{}" é maior que o primeiro valor "{}"'.format(n1, n2))
elif n1 == n2:
    print('\033[34mNão existe valor maior, os dois são iguais "{}".'.format(n1))
