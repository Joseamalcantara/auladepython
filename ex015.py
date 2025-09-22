# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado

kmPercorrido = float(input("Quantos Km foram percorridos: "))
dias = float(input("Quantos dias esteve com o carro: "))

preco = (60 * dias) + (0.15 * kmPercorrido)

msg = f"O valor a ser pago é R$ {preco:.2f}."
linha = "_" * (len(msg) + 4)
print(f"{linha}\n{msg}")
