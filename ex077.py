palavras = ('python', 'curso', 'computador', 'loja', 'internet', 'notebook', 'celular', 'impressora')
vogais = 'aeiouAEIOU'
for palavra in palavras:
    print(f'\nA palavra {palavra} tem as vogais:', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(letra.upper(), end=' ')
