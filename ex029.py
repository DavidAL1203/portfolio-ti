v = float(input('Digite a velocidade do carro: '))
if v > 80:
    print('O carro esta acima do limite de velocidade que é 80km/h. VOCÊ FOI MULTADO!')
    print('O valor da multa, correspondente a sua velocidade é de R${}.'.format((v-80)*7))
else:
    print('Você esta dentro do limite da via!')
print('Tenha um bom dia! Dirija com segurança!')
