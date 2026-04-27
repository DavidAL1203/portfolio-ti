dados = {'nome': str(input('Nome do jogador: ')), 'gols': [], 'total': 0}
partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))
for c in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {c+1}? '))
    dados['gols'].append(gols)
    dados['total'] += gols
print('='*50)
print(dados)
print('='*50)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('=' * 50)
print(f'O jogador {dados['nome']} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    => Na partida {c+1}, fez {dados['gols'][c]} gols.')
print(f'Foi um total de {dados['total']} gols.')
