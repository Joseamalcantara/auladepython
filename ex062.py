print('Gerando uma P.A.')
print('=-'*15)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 1
termos = p
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termos} -> ', end=' ')
        termos += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados!')
