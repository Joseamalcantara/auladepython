# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

msg_par = 'O número {num} é par!'
msg_impar = 'É ímpar!'
num = int(input('Digite um número e vamos saber se é ímpar ou par: '))

msg_par if num % 2 == 0 else msg_par
