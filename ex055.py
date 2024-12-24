maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}º pesso: '))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso liquido foi {maior} Kg')
print(f'O menor peso liquido foi {menor} Kg')
