soma = cont = num = 0
num = float(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = float(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
