# O memso professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

aluno1 = input("Digite o primeiro aluno: ")
aluno2 = input("Digite o segundo aluno: ")
aluno3 = input("Digite o terceiro aluno: ")
aluno4 = input("Digite o quanto aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

msg = f'A ordem apresentada será: {lista}'
linha = "_" * (len(msg) + 4)
print(f"{linha}\n{msg}")
