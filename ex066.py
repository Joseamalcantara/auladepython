soma = cont = 0
while True:
    valor = float(input('Digite um valor (999 para parar): '))
    if valor == 999:
        break
    soma += valor
    cont += 1
print(f'A soma dos {cont} valores foi {soma}')
