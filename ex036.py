# Escreva um programa para aprovar o empréstimo bancário para a compra de um casa. Pergunte o valor da casa,
# O salário do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário ou então
# o empréstimo será negado.

msg = "Vamos analisar se você pode financiar a casa"
print(f"{msg}\n{"-" * len(msg)}")

c = float(input('Valor da casa: R$ '))  # c: Valor da casa
s = float(input('Salário do comprador: R$ '))  # s: Salário
n = int(input('Quantos anos de finaciamento? '))  # n: anos

p = c / (n * 12)  # p: parcela

print(f'Para pagar uma casa de R$ {c:.2f} em {n} anos a prestação será de R$ {p:.2f}')

if p <= (s * 0.3):
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
