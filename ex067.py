while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*50)
    if valor < 0:
        break
    for cont in range(1, 11):
        print(f'{valor} X {cont} = {valor * cont}')
    print('-'*50)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
