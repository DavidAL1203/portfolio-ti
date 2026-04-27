pessoas = []
dado = []
totpessoas = ppesado = pleve = 0
continuar = 'S'
pesos = []
nomes = []
npesados = []
nleves = []
while not continuar == 'N':
    dado.append(input('Nome: '))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    totpessoas += 1
    if dado[1] > ppesado:
        ppesado = dado[1]
        pleve = dado[1]
    if dado[1] < pleve:
        pleve = dado[1]
    dado.clear()
    continuar = input('Deseja continuar? [S/N]').upper()
for c in range(0, len(pessoas)):
    pesos.append(pessoas[c][1])
    nomes.append(pessoas[c][0])
for i, v in enumerate(pesos):
    if v == ppesado:
        npesados.append(nomes[i])
    if v == pleve:
        nleves.append(nomes[i])
print(f'Temos {len(pessoas)} pessoas cadastradas.')
print(f'O maior peso foi de {ppesado:.2f}kg. Peso de: {npesados}')
print(f'O menor peso foi de {pleve:.2f}kg. Peso de: {nleves}')
