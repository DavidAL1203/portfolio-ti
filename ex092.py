from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - ano
dados['ctps'] = int(input('Carteira de trabalho: '))
print('='*50)
if dados['ctps'] <= 0:
    for k, v in dados.items():
        print(f'{k} tem o valor de {v}')
else:
    dados['ano'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Valor do salario: '))
    dados['aposentadoria'] = (dados['ano'] - ano) + 35
    for k, v in dados.items():
        print(f'{k} tem o valor de {v}')
