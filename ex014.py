# Escreva um programa que converte uma temperatura digitada em ºC e converta para ºF.

msg = "Vamos converter a temperatura em ºC para ºF"
print(msg)
tempraturaC = float(input("Digite a temperaturam em ºC: "))

temperaturaF = (tempraturaC * 1.8) + 32


msg_r = f"A temperatura em Fahrenheit é de ºF {temperaturaF}."
linha = "_" * (len(msg_r) + 4)
print(f"{linha}\n{msg_r}")
