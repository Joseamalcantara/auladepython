media = soma = cont = menor = maior = 0
novo = 'S'
while novo == 'S':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        menor = maior = num
    else:
        if menor > num:
            menor = num
        if maior < num:
            maior = num
    novo = str(input('Quer continuar? [S/N] ')).upper()
media = soma / cont
print(f'Você digitou {cont} número e a média foi {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
