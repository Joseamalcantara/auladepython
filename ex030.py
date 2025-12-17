# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número e vamos saber se é ímpar ou par: '))
msg_par = f'O número {num} é par!'
msg_impar = f'O número {num} é ímpar!'


if num % 2 == 0:
    print(f"{"-" * (len(msg_par))}\n{msg_par}")
else:
    print(f"{"-" * (len(msg_impar))}\n{msg_impar}")
