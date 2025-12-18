# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date
nac = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nac

linha = "-" * 25
if idade <= 9:
    print(f'{linha}\nO atleta tem {idade} anos.')
    print(f'Classificação: MIRIM')
elif 9 < idade <= 14:
    print(f'{linha}\nO atleta tem {idade} anos.')
    print(f'Classificação: INFANTIL')
elif 14 < idade <= 19:
    print(f'{linha}\nO atleta tem {idade} anos.')
    print(f'Classificação: JUNIOR')
elif 19 < idade <= 25:
    print(f'{linha}\nO atleta tem {idade} anos.')
    print(f'Classificação: SÊNIOR')
else:
    print(f'{linha}\nO atleta tem {idade} anos.')
    print(f'Classificação: MASTER')
