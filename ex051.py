print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
num = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = num + (10 - 1) * r
for i in range(num, decimo + r, r):
    print(f'{i}', end=' > ')
print('Acabou')
