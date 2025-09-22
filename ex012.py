# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o valor do produto: "))

desconto = preco - (preco * 0.05)
msg = f"O valor do produto depois do desconto é de R$ {desconto:.2f}."
linha = "-" * (len(msg) + 4)

print(f"{linha}\n{msg.center(len(linha))}")
