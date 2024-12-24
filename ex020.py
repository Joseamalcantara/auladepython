from random import shuffle
aluno1 = input('Digite o primeiro aluno: ')
aluno2 = input('Digite o segundo aluno: ')
aluno3 = input('Digite o terceiro aluno: ')
aluno4 = input('Digite o quanto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print(f'A ordem apresentada será: {lista}')
