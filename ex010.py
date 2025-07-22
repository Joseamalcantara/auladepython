# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
msg = "Vamos converte de Reais para Dolar"
print(msg)
reais = float(input("Qual o valor em Reais: R$ "))
dolar = 5.5 * reais
print(f"O valor de R$ {reais:.2f} é de US$ {dolar:.2f}.")
