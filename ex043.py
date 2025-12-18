# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual é a sua altura? '))

imc = peso/(altura ** 2)

msg = f'O IMC dessa pessoa é de {imc:.1F}'
print(f"{"-" * len(msg)}\n{msg}")

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
