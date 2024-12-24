print('-'*40)
print(' '*5, '-Trabalhando com operadores-')
print('-'*40)
print('Operadores de Atribuição')
x = int(input('Vamos da um valor para o x: '))
num = int(input('Digite um número para para resolver alguns problemas: '))
print(f'O valor de x é {x}')
x += num
print(f'Adição {x}')

x = int(input('Vamos da outro valor para o x: '))
x -= num
print(f'subtração {x}')

x = int(input('Vamos da outro valor para o x: '))
x *= num
print(f'Multiplicação {x}')


x = int(input('Vamos da outro valor para o x: '))
x /= num
print(f'Divisão {x:.1f}')

x = int(input('Vamos da outro valor para o x: '))
x //= num
print(f'Divisão inteira {x}')

x = int(input('Vamos da outro valor para o x: '))
x %= num
print(f'Resto da divisão {x}')

x = int(input('Vamos da outro valor para o x: '))
x **= num
print(f'A reslução da expressão é {x}')

