from random import choice
a=input('Digite algo: ')
cor1 = '\033[30m'
cor2 = '\033[31m'
cor3 = '\033[32m'
cor4 = '\033[33m'
cor5 = '\033[34m'
cor6 = '\033[35m'
cor7 = '\033[36m'
cor8 = '\033[37m'
lista = [cor1, cor2, cor3, cor4, cor5, cor6, cor7, cor8]
print('{}O tipo primitivo de "{}" é {}. '.format(choice(lista), a,type(a)))
if a.isalnum(): print('{}{} é alfanumerico'.format(choice(lista), a))
else: print('{}{} não é alfanumerico'.format(choice(lista), a))
if a.isalpha(): print('{}{} é alpha'.format(choice(lista), a))
else: print('{}{} não é alpha'.format(choice(lista), a))
if a.isascii(): print('{}{} é ascii'.format(choice(lista), a))
else: print('{}{} não é ascii'.format(choice(lista), a))
if a.isdigit(): print('{}{} é digito'.format(choice(lista), a))
else: print('{}{} não é digito'.format(choice(lista), a))
if a.islower(): print('{}{} está em minusculo'.format(choice(lista), a))
else: print('{}{} não está em minusculo'.format(choice(lista), a))
if a.isdecimal(): print('{}{} é decimal'.format(choice(lista), a))
else: print('{}{} não é decimal'.format(choice(lista), a))
if a.isidentifier(): print('{}{} é um identificador valido'.format(choice(lista), a))
else: print('{}{} não é um identificador valido'.format(choice(lista), a))
if a.isnumeric(): print('{}{} é numérico'.format(choice(lista), a))
else: print('{}{} não é numérico'.format(choice(lista), a))
if a.isprintable(): print('{}{} é imprimivel'.format(choice(lista), a))
else: print('{}{} não é imprimivel'.format(choice(lista), a))
if a.isspace(): print('{}{} é um espaço'.format(choice(lista), a))
else: print('{}{} não é um espaço'.format(choice(lista), a))
if a.istitle(): print('{}{} está em maiusculo'.format(choice(lista), a))
else: print('{}{} não está em maiusculo'.format(choice(lista), a))
if a.isupper(): print('{}{} contem um ou mais caractere maiusculo'.format(choice(lista), a))
else: print('{}{} não contem nenhum caractere maiusculo'.format(choice(lista), a))
if a.__init_subclass__(): print('{}{} é uma subclasse'.format(choice(lista), a))
else: print('{}{} não é uma subclasse'.format(choice(lista), a))
