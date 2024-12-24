# c: Valor da casa
# s: Salário
# n: anos
# p: parcela
c = float(input('Valor da casa: R$ '))
s = float(input('Salário do comprador: R$ '))
n = int(input('Quantos anos de finaciamento? '))

p = c / (n * 12)

print(f'Para pagar uma casa de R$ {c:.2f} em {n} anos a prestação será de R$ {p:.2f}')

if p <= (s * 0.3):
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
