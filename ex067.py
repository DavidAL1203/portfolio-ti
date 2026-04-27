while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    if tab < 0:
        break
    print(f'{'-'*33}\n'
          f'{tab} X 01 = {tab}\n'
          f'{tab} X 02 = {tab * 2}\n'
          f'{tab} X 03 = {tab * 3}\n'
          f'{tab} X 04 = {tab * 4}\n'
          f'{tab} X 05 = {tab * 5}\n'
          f'{tab} X 06 = {tab * 6}\n'
          f'{tab} X 07 = {tab * 7}\n'
          f'{tab} X 08 = {tab * 8}\n'
          f'{tab} X 09 = {tab * 9}\n'
          f'{tab} X 10 = {tab * 10}\n'
          f'{'-'*33}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
