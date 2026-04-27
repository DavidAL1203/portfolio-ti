valor = float(input('\033[36mInforme o valor do produto: R$'))
if valor <= 0:
    print('\033[31m valor indicado é invalido!')
elif valor >0:
    pagamento = int(input('''\033[36mFORMAS DE PAGAMENTO:
[ 1 ] Dinheiro/PIX (10% de desconto)
[ 2 ] Cartão (Sujeito a juros)
Digite o numero correspondente a forma de pagamento: '''))
    if pagamento != 1 and pagamento != 2:
        print('\033[31mForma de pagamento invalida!')
    elif pagamento == 1:
        print('\033[34mValor final: R${:.2f}'.format(valor - (valor * 10 / 100)))
    elif pagamento == 2:
        avista_parcelado = int(input('''\033[36mFORMAS DE PAGAMENTO:
[ 1 ] À Vista (5% de desconto)
[ 2 ] Parcelado (Sujeito a juros)
Digite o numero correspondente a forma de pagamento: '''))
        if avista_parcelado != 1 and avista_parcelado != 2:
            print('\033[31mForma de pagamento invalida!')
        elif avista_parcelado == 1:
            print('\033[34mValor final: R${:.2f}'.format(valor - (valor * 5 / 100)))
        elif avista_parcelado == 2:
            parcela = int(input('''\033[36mTABELA DE JUROS:
|       2x sem juros ou       |
|  3x ate 12x (20%) de juros  |
Informe em quantas vezes você vai parcelar: '''))
            if parcela < 2 or parcela > 12:
                print('\033[31mA parcela indicada é invalida!')
            elif parcela == 2:
                print('\033[34mValor final: R${:.2f} em 2x de R${:.2f}'.format(valor, valor / 2))
            elif 12 >= parcela > 2:
                print('\033[34mValor final: R${:.2f} em {}x de R${:.2f}'.format(valor + (valor * 20 / 100), parcela,
                                                                        (valor + (valor * 20 / 100)) / parcela))
