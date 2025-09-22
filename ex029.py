# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro? '))

msg_multa = f'Você ultrapassou a velocidade máxima, sua multar é R$ {(velocidade - 80) * 7:.2f}'
msg_despedida = 'Tenha um bom dia! Dirija com segurança!'
linha = '-' * len(msg_multa)

if velocidade > 80:
    print(f'{linha}\n{msg_multa}\n{linha}')
print(msg_despedida)
