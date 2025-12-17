# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input("Qual é o seun nome: ")
msg = f"É um prazer em te conhrcer, {nome}"
linha = f"{"-" * (len(msg) + 2)}"

print(f"{linha}\n{msg}")
