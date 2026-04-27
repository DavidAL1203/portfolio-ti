times = ('flamengo', 'cruzeiro', 'palmeiras', 'baia', 'botafogo', 'mirassol', 'são paulo', 'bragantino',
         'fluminense', 'internacional', 'ceara', 'corinthians', 'gremio', 'atletico-mg', 'vasco da gama',
         'santos', 'ec vitoria', 'juventude', 'fortaleza', 'sport recife')
print(f'Lista de times: {times}')
print('='*100)
print(f'Os 5 primeiros times são: {times[:5]} ')
print('='*100)
print(f'Os 4 ultimos times são: {times[-4:]}')
print('='*100)
print(f'Lista de times em ordem alfabetica: {sorted(times)}')
print('='*100)
print(f'O time palmeiras esta na {times.index('palmeiras')+1} posição.')
