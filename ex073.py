print('-='*150)
brasileirao = (('Athletico', 'Atlético', 'Atlético', 'Bahia', 'Botafogo', 'Corinthians', 'Criciúma', 'Cruzeiro',
               'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras',
               'Red Bull Bragantino', 'São Paulo', 'Vasco da Gama', 'Vitória'))
print(f'Lista de times do Brasileirão: {brasileirao}')
print('-='*150)
print('\n')
print(f'Os 5 primeiros são {brasileirao[:6]}')
print(f'Os quanto ultimos são {brasileirao[-4:]}')
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print(f'O Bahia está na {brasileirao.index("Bahia") + 1}º posição')
