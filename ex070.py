continuar = total = maisdemil = maisbarato = 0
sn = mb = str
print(f'{'-'*30}\n'
      f'{'LOJA SUPER BARATÃO':^30}\n'
      f'{'-'*30}')
while True:
    produto = input('Nome do produto: ')
    valor = int(input('Preço: R$'))
    total += valor
    if valor > 1000:
        maisdemil += 1
    if maisbarato == 0:
        maisbarato = valor
        mb = produto
    elif valor < maisbarato:
        maisbarato = valor
        mb = produto
    while continuar == 0:
        sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if sn == 'N':
            continuar = 1
        elif sn == 'S':
            continuar = 1
        else:
            print('Opção invalida!')
    continuar = 0
    if sn == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisdemil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {mb} que custa R${maisbarato:.2f}')
