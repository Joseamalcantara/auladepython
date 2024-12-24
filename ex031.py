km = float(input('Qual a distância em Km? '))
if km <= 200:
    print(f'Foi {km} Km, o preço das passagem é R$ {km * 0.5:.2f}')
else:
    print(f'Foi {km} Km, o preço das passagem é R$ {km * 0.45:.2f}')

