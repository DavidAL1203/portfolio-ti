def escreva(msg):
    print('~'*(len(msg)+4))
    print(f'  {msg}')
    print('~'*(len(msg)+4))


for c in range(0, 3):
    escreva(str(input('Digite algo: ')))
