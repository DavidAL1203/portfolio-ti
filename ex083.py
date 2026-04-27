expr = str(input('Digite uma expressão: '))
lista = []
for c in range(0, len(expr)):
    if expr[c] == '(':
        lista.append(expr[c])
    elif expr[c] == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(expr[c])
            break
if len(lista) == 0:
    print('A expressão está correta!')
else:
    print('A expressão está errada!')
