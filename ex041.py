from datetime import date
nac = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nac

if idade <= 9:
    print(f'O atleta tem {idade} anos.')
    print(f'Classificação: MIRIM')
elif 9 < idade <= 14:
    print(f'O atleta tem {idade} anos.')
    print(f'Classificação: INFANTIL')
elif 14 < idade <= 19:
    print(f'O atleta tem {idade} anos.')
    print(f'Classificação: JUNIOR')
elif 19 < idade <= 25:
    print(f'O atleta tem {idade} anos.')
    print(f'Classificação: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos.')
    print(f'Classificação: MASTER')
