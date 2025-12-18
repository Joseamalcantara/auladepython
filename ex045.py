from random import randint
print("""Sua opção
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

itens = ['Pedra', 'Papel', 'Tesoura']

computador = randint(0, 2)
jogador = int(input('Qual a sua escolha: '))
linha = '-='*20

print(f'{linha}\nO COMPUTADOR ESCOLHEU {itens[computador]}\nO JOGADOR ESCOLHEU {itens[jogador]}\n{linha}')

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Você ganhou!')
    elif jogador == 2:
        print('O computador ganhou!')
    else:
        print('Jogada Invalida!')
elif computador == 1:
    if jogador == 0:
        print('Você ganhou!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Você ganhou!')
    else:
        print('Jogada Invalida!')
elif computador == 2:
    if jogador == 0:
        print('Você ganhou!')
    elif jogador == 1:
        print('O computador ganhou!')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Invalida!')

