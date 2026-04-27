lista = []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if len(lista) == 0:
        lista.append(valor)
        print('Valor adicionado ao final da lista')
    else:
        if valor >= max(lista):
            lista.append(valor)
            print('Valor adicionado ao final da lista')
        elif valor <= min(lista):
            lista.insert(0, valor)
            print('Valor adicionado no inicio da lista')
        elif min(lista) < valor < max(lista) and valor < lista[1]:
            lista.insert(1, valor)
            print('Valor adicionado na posição 1 da lista')
        elif lista[1] < valor < lista[2]:
            lista.insert(2, valor)
            print('Valor adicionado na posição 2 da lista')
        elif lista[2] < valor < lista[3]:
            lista.insert(3, valor)
            print('Valor adicionado na posição 3 da lista')
print(lista)
