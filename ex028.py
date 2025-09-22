# Escreva um programa que faç o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foio número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

linha = '-=' * 40
msg_pensar = 'Vou pensar um um número entre 0 e 5. Tente adivinhar...'

print(f"{linha}\n{msg_pensar}")
sleep(3)
num = int(input('Em que número eu pensei? '))
numero_aleatorio = randint(1, 5)

if num != numero_aleatorio:
    print(f'GANHEI! Eu pensei no número {numero_aleatorio} e não no {num}!')
else:
    print(f'Você ganhou! Eu pensei no número {numero_aleatorio} também :(')
