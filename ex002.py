# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input("Digite o seu nome: ")
msg = f"É um prazer em te conhrcer, {nome}"
linha = f"+{"-" * (len(msg) + 4)}+"

print(f"{linha}\n|{msg.center(len(msg) + 4)}|\n{linha}")
