cont = 0
soma = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        cont += 1
        soma += i
print(f'A quantidade de números impares é {cont} e a soma é {soma}!')
