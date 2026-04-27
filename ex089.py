from time import sleep
lista = []
nomes = []
notas = []
medias = []
continuar = 'S'
while not continuar == 'N':
    nomes.append(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    nomes.append(notas[:])
    lista.append(nomes[:])
    nomes.clear()
    notas.clear()
    continuar = str(input('Quer continuar? [S/N] ')).upper()
print('-'*25)
print('Nº.  NOME           MÉDIA')
print('-'*25)
for c in range(0, len(lista)):
    medias.append((lista[c][1][0] + lista[c][1][1]) / 2)
    print(f'{c}    {lista[c][0]:<15} {medias[c]:.1f}')
print('-'*50)
aluno = int
while not aluno == 999:
    aluno = int(input('Mostrar notas de qual aluno? (999 para sair): '))
    if aluno == 999: break
    if aluno >= len(lista) or aluno < 0:
        print('Aluno inexistente.')
    else:
        print(f'Notas de {lista[aluno][0]} são {lista[aluno][1]}')
    print('-'*50)
print('Saindo...')
print('-'*50)
sleep(1)
print('<<< VOLTE SEMPRE >>>')
