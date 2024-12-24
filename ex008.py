metros = float(input('Digite um número em metros: '))
km = metros/1000
hm = metros/100
dam = metros/10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print(f'A medida em {metros}m corresponde a')
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')
