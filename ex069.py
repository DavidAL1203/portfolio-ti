continuar = str
validarsexo = contidade = conthomens = contmulheres = 0
while True:
    print('=' * 20)
    print('CADASTRE UMA PESSOA')
    print('=' * 20)
    idade = int(input('Idade: '))
    if idade > 18:
        contidade += 1
    while validarsexo != 1:
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        if sexo == 'M':
            conthomens += 1
            validarsexo = 1
        elif sexo == 'F':
            if idade < 20:
                contmulheres += 1
            validarsexo = 1
        else:
            print('Opção invalida! Digite novamente.')
    validarsexo = 0
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('Continuar? [S/N]: ')).strip().upper()[0]
        if continuar == 'N':
            break
        elif continuar == 'S':
            pass
        else:
            print('Opção invalida! Digite novamente.')
    if continuar == 'N':
        break
    continuar = 'a'
print(f'{'='*5} FIM DO PROGRAMA {'='*5}')
print(f'Total de pessoas com mais de 18 anos: {contidade}')
print(f'Ao todo temos {conthomens} homens cadastrados')
print(f'E temos {contmulheres} mulheres com menos de 20 anos')
