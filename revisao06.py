print('-'*40)
print(' '*5, '-Trabalhando com operadores-')
print('-'*40)
print('Operadores Associação')

lista = [1, 2, 3, 4, 5]
print(lista)
num = int(input('Digite um número e veremos se está na lista: '))
print(f'O {num} está na lista? {num in lista}')
print(f'O {num} não está na lista? {num not in lista}')

