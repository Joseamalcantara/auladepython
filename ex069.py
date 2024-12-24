s = i = m = f = 0
continua = ' '
while continua not in 'N':
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade > 18:
        i += 1
    sexo = input('[M/F] ').upper().strip()
    if sexo == 'M':
        m += 1
    if sexo == 'F' and idade < 20:
        f += 1
    print('-' * 30)
    continua = input('Quer continuar? [S/N] ').upper().strip()
print(f'Total de pessoas com mais de 18 anos: {i}')
print(f'Ao todo temos {m} homem cadastrado(s)')
print(f'E temos {f} mulher(es) com menos de 20 anos')
