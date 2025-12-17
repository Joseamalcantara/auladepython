# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa
import math
from idlelib.macosx import hideTkConsole

msg = "Vamos calcular a hipotenusa do triângulo"
cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adjacente = float(input("Digite o cateto adjacente: "))

hipotenusa = math.hypot(cateto_adjacente, cateto_oposto)

msg = f"O valor da hipotenusa é {hipotenusa:.2f}"
linha = "_" * (len(msg) + 10)
print(f"{msg}\n{linha}\n{msg} ou {math.trunc(hipotenusa)}")
