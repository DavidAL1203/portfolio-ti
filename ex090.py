aluno = {'nome': str(input('Nome: ')),
         'media': float(input('Média: '))}
print(f'Nome é igual a {aluno['nome']}')
print(f'Média é igual a {aluno['media']}')
print('Situação é igual a ', end='')
if aluno['media'] >= 7:
    print('Aprovado')
elif aluno['media'] >= 5:
    print('Recuperação')
else:
    print('Reprovado')
