# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
print("Vamos ver o tipo de informação e o que e suas composições baseadas no que você digitou.")
valor = input("Digite algo: ")
print(f"Você digitou um tipo ", type(valor))
msgObs = "Obs.: Mesmo você digitando número, sempre vai ser 'str', pois não declarei na variável"
print(f"{msgObs}\n{"-" * (len(msgObs) + 4)}")

print(f"Só tem número: {valor.isnumeric()}")
print(f"É espaço vazio: {valor.isspace()}")
print(f"É um número décimal: {valor.isdecimal()}")

