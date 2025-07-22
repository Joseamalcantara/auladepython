# Um professor quer sortear um dos seus quatro alunos para pagar o quadro. Faça um programa que ajude ele, lembrando o nome deles e escreva o nome escolhido.

from random import choice
aluno1 = input("O primeiro aluno: ")
aluno2 = input("O segundo aluno: ")
aluno3 = input("O terceiro aluno: ")
aluno4 = input("O quanto aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]
msg = f"O aluno escolhido foi: {choice(lista)}"

linha = "_" * (len(msg) + 4)
print(f"{linha}\n{msg}")
