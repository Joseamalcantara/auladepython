# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado

msg = "Vamos calcular o valor a ser pago"
print(msg)
kmPercorrido = float(input("Quantos Km foram percorridos: "))
dias = float(input("Quantos dias esteve com o carro: "))

preco = (60 * dias) + (0.15 * kmPercorrido)

msg_r = f"O valor a ser pago é R$ {preco:.2f}."
linha = "_" * (len(msg) + 4)
linha_fim ="^" * len(linha)
print(f"{linha}\n{msg_r}\n{linha_fim}")
