print('-='*30)
print('Vamos mostrar qual o maior valor e o menor valor')
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))

# Saber qual o maior valor dos três
if valor1 > valor2 and valor1 > valor3:
    maior = valor1

elif valor2 > valor1 and valor2 > valor3:
    maior = valor2

elif valor3 > valor1 and valor3 > valor2:
    maior = valor3

# Saber o menor valor dos três

if valor1 < valor2 and valor1 < valor3:
    menor = valor1

elif valor2 < valor1 and valor2 < valor3:
    menor = valor2

elif valor3 < valor1 and valor3 < valor2:
    menor = valor3

print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
