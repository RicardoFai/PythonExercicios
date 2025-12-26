times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol',
         'Fluminense', 'Botafogo', 'Bahia', 'São Paulo',
         'Grêmio', 'Bragantino', 'Corinthia', 'Atlético-MG',
         'Vasco', 'Ceará', 'internacional', 'Vitória',
         'Santos', 'Fortaleza', 'Juventude', 'Sport' )
print('-=' * 15)
print(f'listas de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Time em ordem alfabéticas {sorted(times)}')
print('-=' * 15)
print(f'O Mirassol está na {times.index("Mirassol")+1}ª posição')

