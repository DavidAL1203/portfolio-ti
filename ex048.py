soma = 0
a = 0
for c in range(1, 501):
    if c == 3:
        soma = 3
        a += 1
    elif c % 2 != 0 and c % 3 == 0:
        soma += c
        a += 1
print('\033[34mA soma de todos os {} valores solicitados é: \033[31m{}\033[34m!'.format(a, soma))
