print('Digite um número para')
num = int(input('Calcular o seu fatorial: '))
c = num
f = 1
print(f'Calculando {num}! = ', end='')
while c > 0:
    print(f'{c}', end="")
    print(f' X ' if c > 1 else ' =', end=' ')
    f *= c
    c -= 1
print(f'{f}')
