from random import randint

print('-=' * 40)
print('Vou pensar um um número entre 0 e 5. Tente adivinhar...')
print('-=' * 40)
num = int(input('Em que número eu pensei? '))
numero_aleatorio = randint(1, 5)

if num != numero_aleatorio:
    print(f'GANHEI! Eu pensei no número {numero_aleatorio} e não no {num}!')
else:
    print(f'Você ganhou! Eu pensei no número {numero_aleatorio} também :(')
