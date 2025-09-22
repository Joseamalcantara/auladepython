# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual é o seu salário? R$ "))
novoSalario = salario - (salario * 0.15)
msg = f"Seu novo salário será de R$ {novoSalario:.2f}"

linha = "_" * (len(msg) + 4)
print(f"{linha}\n{msg.center(len(linha))}")
