from datetime import date
nascimento = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
alistamento = nascimento + 18
falta = idade - 18

if idade < 18:
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano}.')
    print(f'Ainda faltam {falta} anos para alistamentos')
    print(f'Seu alistamento será em {ano + falta}')
elif idade > 18:
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano}.')
    print(f'Você já deveria ter se alistado há {falta} anos')
    print(f'Seu alistamento foi em {alistamento}')
else:
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano}.')
    print(f'Você tem que se alistar IMEDIATAMENTE!')
