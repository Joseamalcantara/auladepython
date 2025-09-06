# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex.: Digite um número: 1834
# unidade: 4 dezena 3 centena: 8 milhar: 1
num = int(input("Digite um número: "))
n = str(num)
print(f"Analisando o número {num}...")
print(f"unidade {n[3]}")
print(f"Dezena: {n[-2]}")
print(f"Centena: {n[1]}")
print(f"Milhar: {n[0]}")
print(n[0:4:2])
