num = int(input('Digite um número e vamos ver se é primo: '))
cont = 0
for i in range(1, num+1):
    if num % i == 0:
        cont += 1
print(f'O número {num} foi dividido {cont} vezes')
if cont == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO!')
