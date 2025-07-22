# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
angulo = float(input("Digite o ângulo que deseja calcular: "))
msg = f"O Seno, Cosseno e Tangente de {angulo} é:\nSeno: {sin(radians(angulo)):.2f}\nCosseno: {cos(radians(angulo)):.2f}\nTangente: {tan(radians(angulo)):.2f}"
linha = "_" * (len(msg) + 4)
print(f"{linha}\n{msg}")
