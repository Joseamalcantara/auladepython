salario = float(input('Qual o salário do funcionário? R$ '))
reajuste = salario + ((salario * 15)/100)
print(f'Um funcionário que ganhava R$ {salario:.2f}, com 15% de aumento, passa a receber R$ {reajuste}')
