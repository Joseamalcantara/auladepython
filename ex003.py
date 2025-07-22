# Vamos somar dois números inteiros Você irá digitar dois números para calcularmos a soma.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
msg = f"O resultado da soma de {num1} e {num2} é {soma}."
linha = f"+{"-" * (len(msg) + 6)}+"

print(f"{linha}\n|{msg.center(len(linha) - 2)}|\n{linha}")

