# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m^2

altura = float(input("Digite a altura: "))
largura = float(input("Digite a largura: "))

area = largura * altura
tinta = area / 2

print(f"A soma dos dois numeros é {area:.2f}m²\nPara pintar a parede, você precisará de {tinta}l de tinta")
