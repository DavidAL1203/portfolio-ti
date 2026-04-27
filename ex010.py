nome=input('Digite seu nome: ')
carteira=float(input('Digite quanto tem em sua carteira: R$'))

print('Considerando o preço do dollar a \033[32mUS$3.27\033[m, {} pode comprar \033[31mUS${:.2f}\033[m com os \033[36mR${:.2f}\033[m disponiveis em sua carteira!'.format(nome, carteira/3.27, carteira))
