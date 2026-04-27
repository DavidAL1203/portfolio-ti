continuar = 'S'
lista = []
mulheres = []
acimamedia = []
while not continuar == 'N':
    dados = {'nome': str(input('Nome: ')),
             'sexo': str(input('Sexo: ')),
             'idade': int(input('Idade: ')),}
    if dados['sexo'] in 'Ff':
        mulheres.append(dados['nome'])
    lista.append(dados)
    del dados
    continuar = str(input('Deseja continuar? [S/N]')).upper()
print('='*50)
somaidades = 0
for c in range(0, len(lista)):
    somaidades += lista[c]['idade']
media = somaidades / len(lista)
for c in range(0, len(lista)):
    if lista[c]['idade'] > media:
        acimamedia.append(lista[c])
print(f'=> O grupo tem {len(lista)} pessoas.')
print(f'=> A média de idade é de {media:.2f} anos.')
print(f'=> As mulheres cadastradas foram: ', end='')
for i in mulheres:
    print(f'{i}', end=' ')
print()
print(f'=> Lista das pessoas que estão acima da média:')
for i in acimamedia:
    print(i)
