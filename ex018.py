from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que deseja calcular: '))
print(f'O Seno, Cosseno e Tangente de {angulo} é respectivamente {sin(radians(angulo)):.2f}, {cos(radians(angulo)):.2f}, {tan(radians(angulo)):.2f}')
