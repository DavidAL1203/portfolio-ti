import random
n1=input('Digite o nome do primeito do aluno: ')
n2=input('Digite o nome do segundo do aluno: ')
n3=input('Digite o nome do terceito do aluno: ')
n4=input('Digite o nome do quarto do aluno: ')
lista= [n1,n2,n3,n4]
random.shuffle(lista)
print(lista)
