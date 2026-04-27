reta1 = int(input('\033[34mDigite o comprimento da primeira reta: \033[m'))
reta2 = int(input('\033[34mDigite o comprimento da segunda reta: \033[m'))
reta3 = int(input('\033[34mDigite o comprimento da terceira reta: \033[m'))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    if reta1 == reta2 == reta3:
        print('\033[36mAs três retas podem formar um triângulo equilátero')
    elif reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1:
        print('\033[36mAs três retas podem formar um triângulo Isósceles')
    elif reta1 != reta2 != reta3:
        print('\033[36mAs três retas podem formar um triângulo Escaleno')
else:
    print('\033[31mAs três retas não podem formar um triângulo!\033[m')
