# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes apareceu a letra "A";
# Em que posição ela aparecu a primeira vez;
# Em que posção ela apareceu a última vez

frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find("A")+1}')
print(f'A ultima letra A apareceu na posição {frase.rfind("A")+1}')
