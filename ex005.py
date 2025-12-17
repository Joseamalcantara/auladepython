# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

msg = "Vamos mostrar o antecesor e o sucessor do número que você digitar"
print(msg)
num = int(input("Digite um número: "))
antecessor = num - 1
sucessor = num + 2
msg_r = f"O antecessor e o sucessor de {num}, respectivamente é {antecessor} e {sucessor} "
linha = "-" * (len(msg_r) + 2)

print(f"{linha}\n{msg_r}")
