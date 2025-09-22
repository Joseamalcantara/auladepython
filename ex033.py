# Faça um programa que leia três números e mostre qual é a maior e qual é o menor.

titulo = 'Vamos mostrar qual o maior valor e o menor valor'
linha = "=-" * len(titulo)

print(f"{linha}\n{titulo}")
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))

# Totos os números são iguais
if valor1 == valor2 == valor3:
    print("Todos os valores são iguais")
# Saber qual o maior valor dos três
else:
    maior = max(valor1, valor2, valor3)
    menor = min(valor1, valor2, valor3)

    print(f"\nO maior valor é {maior}\nO menor valor é {menor}")
