#sem variaveis
m1=float(input('digite um valor em metros: '))
print('\033[31mValor em kilómetros: {} km. \nValor em hectómetros: {} hm. \nValor em decámetros: {} dam. \nValor em metros: {} m. \nValor em decímetros: {} dm. \nValor em centimereos: {} cm. \nValor em milimetros: {} mm.'.format(m1/1000, m1/100, m1/10, m1, m1*10, m1*100, m1*1000))
print('')

#com variaveis
m2=float(input('digite um novo valor em metros:'))
km= m2/1000
hm= m2/100
dam= m2/10
dm= m2*10
cm= m2*100
mm= m2*1000
print('\033[7:37:40mValor em kilómetros: {} km.'.format(km))
print('Valor em hectómetros: {} hm.'.format(hm))
print('Valor em decámetros: {} dam.'.format(dam))
print('Valor em metros: {} mm.'.format(m2))
print('Valor em decímetros: {} dm.'.format(dm))
print('Valor em centímetros: {} cm.'.format(cm))
print('Valor em milimetros: {} mm.'.format(mm))
