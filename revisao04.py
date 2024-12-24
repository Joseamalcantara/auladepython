print('-'*40)
print(' '*5, '-Trabalhando com operadores-')
print('-'*40)
print('Operadores Lógicos')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))
num4 = int(input('Digite outro número: '))

print(f'Vamos comparar e fazer uma tabela verdade')
print(f'{num4} > {num2} ^ {num2} > {num3}: {(num4 > num2) and (num2 > num3)}')
print(f'{num4} > {num2} ou {num2} < {num3}: {(num4 > num2) or (num2 > num3)}')
print(f'{num4} < {num2}: {not (num4 < num2)}')
