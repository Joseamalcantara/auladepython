velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print(f'Você ultrapassou a velocidade máxima, sua multar é R$ {(velocidade - 80) * 7:.2f}')
print('Tenha um bom dia! Dirija com segurança!')
