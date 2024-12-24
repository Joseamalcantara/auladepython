num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))

tupla = (num1, num2, num3, num4)

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}º posição')
else:
    print('Não temos o valor 3')
print(f'Os valores pares digitados foram ', end='')

for i in tupla:
    if i % 2 == 0:
        print(i, end='')
