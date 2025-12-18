# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

linha = '-'

media = (nota1 + nota2) / 2

msg = f'Tirando {nota1} e {nota2}, a média do aluno é {media}'
print(f"{linha * (len(msg) + 2)}\n{msg}")
if media >= 7:
    print('O aluno está APROVADO.')
elif media >= 5 and media < 7:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está REPR0VADO.')

