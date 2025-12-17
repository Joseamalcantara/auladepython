# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex.: Digite um número: 1834
# unidade: 4 dezena 3 centena: 8 milhar: 1

import time
print("Vamos mostra a unidade, dezena, centena e milha do número dado")
num = int(input("Digite um número de quatro algarismo: "))
n = str(num)

print(f"Analisando o número {n}...")
time.sleep(3)
print(f"unidade {n[3]}")
print(f"Dezena: {n[-2]}")
print(f"Centena: {n[1]}")
print(f"Milhar: {n[0]}")
