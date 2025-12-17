# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
msg = "Vamos calcular o dobro, triplo e a raiz do número dado."

num = int(input(f"Digite um número e daresmo o seu dobro e triplo: "))
dobro = num * 2
triplo = num * 3
raiz = num ** 1/2

print(f"\nO dobro de {num} é {dobro}\nO triplo de {num} é {triplo}\nA raiz quadrada de {num} é {raiz:.0f}")
