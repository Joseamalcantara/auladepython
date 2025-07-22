# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa
import math

cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adjacente = float(input("Digite o cateto adjacente: "))

hipotenusa = math.hypot(cateto_adjacente, cateto_oposto)

msg = f"O valor da hipotenusa é {hipotenusa:.2f}"
linha = "_" * len(msg)
print(f"{linha}\n{msg} ou {math.trunc(hipotenusa)}")

