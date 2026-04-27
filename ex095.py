continuar = ''
lista = []
while not continuar == 'N':
    dados = {'nome': str(input('Nome do jogador: ')), 'gols': [], 'total': 0}
    partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {c+1}? '))
        dados['gols'].append(gols)
        dados['total'] += gols
    lista.append(dados)
    del dados
    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção Invalida! digite apenas S ou N:')).upper()[0]
    if continuar == 'N': break
    continuar = ''
print('='*50)
print(lista)
print('='*50)
print('cod  nome           total   gols por partida ')
for c in range(0, len(lista)):
    print(f'{c:<5}{lista[c]['nome']:<15}{lista[c]['total']:<8}{lista[c]['gols']}')
print('='*50)
cod = int
while True:
    cod = int(input('Mostrar dados de qual jogador? '))
    if cod == 999: break
    if cod not in range(0, len(lista)):
        print('Opção Invalida!')
    else:
        print(f'-- Levantamento de {lista[cod]['nome']}')
        for c in range(0, len(lista[cod]['gols'])):
            print(f'No jogo {c+1} fez {lista[cod]['gols'][c]} gols.')
    print('='*50)
print('='*50)
print('<<<VOLTE SEMPRE>>>')
