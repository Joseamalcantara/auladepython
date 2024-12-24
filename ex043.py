peso = float(input('Qual o seu peso? '))
altura = float(input('Qual é a sua altura? '))

imc = peso/(altura ** 2)

print(f'O IMC dessa pessoa é de {imc:.1F}')

if imc < 18.5:
    print(f'Você está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
else:
    print('Você está OBESIDADE MORBIDA')
