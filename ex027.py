# Faça um programa que leia o nome completo de uma pessoa, mostrando um seguida o primeiro e o último nome separadamente.
# Ex.: Ana Maria de Souza
# primeiro nome: Ana
# segundo nome: Souza

n = input('Digite seu nome completo: ').strip()
nome = n.split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu útimo nome é {nome[-1]}')
