# Crie um programa que escreva "Olá, Mundo!" na tela.

msg = "Olá, Mundo!"
linha = f"+{"-" * (len(msg) + 10)}+"

print(f"{linha}\n|{msg.center(len(msg) + 10)}|\n{linha}")
