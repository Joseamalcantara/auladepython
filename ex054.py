from datetime import date
maioridade = 0
menoridade = 0
for i in range(1, 8):
    ano = int(input(f'Em que ano a {i}º pessoa nasceu? '))
    idade = date.today().year - ano
    if idade >= 18:
        maioridade += 1
    else:
        menoridade +=1
print(f'Ao todo tivemos {maioridade} pessoas maiores de idade')
print(f'E também tivemos {menoridade} pessoas menores de idade')
