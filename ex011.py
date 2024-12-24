largura = float(input('A largura da parede em metros: '))
altura = float(input('A Altura da parede em metros: '))

area = altura * largura
litros = area / 2

print(f'Com altura de {altura} e {largura} a sua parede tem {area}m^2')
print(f'Com uma área {area}m^2 vai ser gasto {litros} litros')
