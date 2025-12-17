# Desenvolva um programa que leia as duas notas de um aluno

msg = "Vamos calcular a média de duas notas de um aluno."
linha = "-" * len(msg)
print(msg)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"{linha}\nA média do aluno é {media:.1f}")
