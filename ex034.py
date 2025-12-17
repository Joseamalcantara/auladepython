# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

print("Vamos calcular o seu aumento")
salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    novo = (salario * 0.15) + salario
else:
    novo = (salario * 0.1) + salario

print(f'Quem ganhava {salario:.2f} passa a ganhar R$ {novo:.2f}')

