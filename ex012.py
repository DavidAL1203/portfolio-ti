n=input('Digite o nome do produto: ')
p=float(input('Digite o preço do produto: R$'))
print('O preço normal de {} é R${:.2f} e com 5% de desconto fica R${:.2f}!'.format(n, p, p-(p*5/100)))
