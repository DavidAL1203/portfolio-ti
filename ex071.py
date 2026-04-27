print(f'{'='*30}\n'
      f'{'BANCO CEV':^30}\n'
      f'{'='*30}')
valor = int(input('Digite o valor a ser sacado: R$'))
c50 = c20 = c10 = c1 =0
while True:
    if valor >= 50:
        c50 += 1
        valor -= 50
    elif valor >= 20:
        c20 += 1
        valor -= 20
    elif valor >= 10:
        c10 += 1
        valor -= 10
    elif valor >= 1:
        c1 += 1
        valor -= 1
    else:
        break
if c50 > 0:
    print(f'Total de {c50} cédulas de R$50,00')
if c20 > 0:
    print(f'Total de {c20} cédulas de R$20,00')
if c10 > 0:
    print(f'Total de {c10} cédulas de R$10,00')
if c1 > 0:
    print(f'Total de {c1} cédulas de R$1,00')
print(f'{'='*30}\n'
      f'Volte sempre ao banco CEV! Tenha um bom dia!')
