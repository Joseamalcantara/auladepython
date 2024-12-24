from random import randint
sorteados = [randint(0, 10) for i in range(5)]
print('Os valores sorteados foram: ', end='')
for n in sorteados:
    print(f' {n} ', end='')

print(f'\nO maior valor sorteado foi {max(sorteados)}')
print(f'O menor valor sorteado foi {min(sorteados)}')
