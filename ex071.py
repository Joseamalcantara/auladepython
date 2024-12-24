print('='*50)
print('{:^50}'.format('BANCO CEV'))
print('='*50)
valor = int(input('Que valor você quer sacar? R$ '))  # 50, 20, 10, 1
total = valor
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('='*50)
print('Volter sempre ao Banco')
