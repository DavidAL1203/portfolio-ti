def maior():
    mai = tot = 0
    for num in numeros:
        tot += 1
        if num > mai:
            mai = num
    print(f'Os números digitados foram {numeros}.\n'
          f'O Total de números digitados foi {tot}.\n'
          f'Entre eles o maior valor foi {mai}!')


numeros = ()
while True:
    n = int(input('Digite um número (999 Interrompe!): '))
    if n == 999:
        break
    numeros = numeros + (n,)
maior()
