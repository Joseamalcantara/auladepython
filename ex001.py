msg_q = "Crie um programa que escreva - Olá, Mundo! - na tela."
msg = "Olá, Mundo!"
linha = f"+{"-" * (len(msg_q) + 3)}+"

print(f"{linha}\n{msg_q.center(len(linha))}\n{linha}\n{msg}")
