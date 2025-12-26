Primeiro = int(input('Primeiro termo: '))
Razão = int(input('Razão: '))
décimo = Primeiro + (10 - 1) * Razão
for c in range(Primeiro, décimo + Razão, Razão):
    print('{}'.format(c), end= '- ')
print('Acabou!')


