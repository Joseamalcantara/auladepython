# Escreva um programa que converte uma temperatura digitada em ºC e converta para ºF.

tempraturaC = float(input("Digite a temperaturam em ºC: "))

temperaturaF = (tempraturaC * 1.8) + 32

msg = f"A temperatura em Fahrenheit é de ºF {temperaturaF}."
linha = "_" * (len(msg) + 4)
print(f"{linha}\n{msg}")

