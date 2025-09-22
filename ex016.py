# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

num_real = float(input("Digite um número qualquer: "))

msg = f"A parte inteira de {num_real} é {trunc(num_real)}"
linha = "_" * len(msg)
print(f"{linha}\n{msg}")
