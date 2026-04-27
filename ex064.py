n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        cont += 1
        soma += n
print('Foram digitados {} números e a soma deles foi {}!'.format(cont, soma))
