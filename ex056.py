i = 0
mais_velho = 0
nome_velho = ""
mulheres = 0
for p in range(1, 5):
    print('-'*5, f'{p}º PESSOA', '-'*5)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    i += idade
    sexo = input('Sexo: [M/F]: ').upper()

    if sexo == 'M' and mais_velho < idade:
        mais_velho = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1


media_Idade = i / 4

print(f'A média de idade do grupo é de {media_Idade} anos.')
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_velho}')
print(f'Ao todo são {mulheres} mulheres com menos de 20 anos')
