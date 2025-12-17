# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

msg = "Vamos analizar se vai alistar no serviço militar"
linha = ("-" * (len(msg) + 5))
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
