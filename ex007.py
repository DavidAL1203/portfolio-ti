nome=input('Digite o nome do(a) aluno(a): ')
nota1=float(input('Digite a primeira nota do(a) aluno(a): '))
nota2=float(input('Digite a segunda nota do(a) aluno(a): '))
if (nota1 + nota2) / 2 < 70:
    print('A media das notas do(a) aluno(a) \033[36m{}\033[m é \033[31m{:.2f}\033[m!'.format(nome, (nota1+nota2)/2))
if 70 <= (nota1 + nota2) / 2 < 100:
    print('A media das notas do(a) aluno(a) \033[36m{}\033[m é \033[32m{:.2f}\033[m!'.format(nome, (nota1 + nota2) / 2))