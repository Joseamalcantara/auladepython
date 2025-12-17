# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas

print("Vamos calcular o valor da passagem")
km = float(input('Qual a distância em Km? '))
preco_viagens_curtas = f'Foi {km} Km, o preço das passagem é R$ {km * 0.5:.2f}'
preco_viagens_longas = f'Foi {km} Km, o preço das passagem é R$ {km * 0.45:.2f}'

if km <= 200:
    print(preco_viagens_curtas)
else:
    print(preco_viagens_longas)
