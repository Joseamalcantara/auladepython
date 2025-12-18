# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

print('-='*20)
print('Analisandor de Triângulos')
print('-='*20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos assima PODEM FORMAR triângulos!')
    if a == b and a == c and b == c:
        print('O triãngulo é equilátero')
    elif a != b and a != c and b != c:
        print('O triãngulo é escaleno')
    else:
        print('O triãngulo é isoceles')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulos!')
