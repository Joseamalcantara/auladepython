# s: é para associar a salário;

s = float(input('Qual é o salário do funcionário? R$ '))
if s <= 1250:
    novo = (s * 0.15) + s
else:
    novo = (s * 0.1) + s

print(f'Quem ganhava {s:.2f} passa a ganhar R$ {novo:.2f}')

