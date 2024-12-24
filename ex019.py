from random import choice
aluno1 = input('O primeiro aluno: ')
aluno2 = input('O segundo aluno: ')
aluno3 = input('O terceiro aluno: ')
aluno4 = input('O quanto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
print(f'O aluno escolhido foi {choice(lista)}')
