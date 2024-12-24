from random import randint
print('-='*50)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*50)
vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = (input('Par ou ímpar? [P/I] ')).upper().strip()
    computador = randint(1, 10)
    total = computador + jogador
    print('-' * 100)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=" ")
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 100)
    if total % 2 == 0 and escolha == 'P' or total % 2 != 0 and escolha == 'I':
        print('Você VENCEU!')
        vitoria += 1
    else:
        print('Você PERDEU!')
        print('=-' * 50)
        print(f'GAME OVER! Você venceu {vitoria} vezes.')
        break
    print('Vamos jogar novamente...')
