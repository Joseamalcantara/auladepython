print('Gerando uma P.A.')
print('=-'*15)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
n = 0
t = 0
while n < 10:
    t += r
    n += 1
    print(f'{t} -> ', end=' ')
print('FIM')
