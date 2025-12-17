# crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome

import time
nome = str(input("Digite o seu nome completo: ")).strip()
print("Analisando seu nome...")
time.sleep(4)
print(f"Seu nome em letras maiúsculas é {nome.upper()}")
print(f"Seu nome em letras menúculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(" ")}")
print(f"Seu primeiro nome tem {nome.find(" ")}")

separa = nome.split()

print(separa)
print('-' * 15, 'tipo 2', '-' * 15)
print(f'Seu primeiro nome é {separa[0], len(separa[0])}')
