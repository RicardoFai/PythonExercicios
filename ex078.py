listaum = []
mai = 0
men = 0
for c in range(0, 5):
    listaum.append(int(input(f'Digite um valor na Posição {c}: ')))
    if c == 0:
        mai = men = listaum[c]
    else:
        if listaum[c] > mai:
            mai = men = listaum[c]
        if listaum[c] < men:
            men = listaum[c]
print('=-' * 30)
print(f'Você digitou os valores {listaum}' )
print(f'O maior valor digitado foi {mai} nas posições', end='' )
for i, v in enumerate(listaum):
    if v == mai:
        print(f'{i}...', end='')
print(f'O menor valor digitado foi {men} nas posições', end='' )
for i, v in enumerate(listaum):
    if v == men:
        print(f'{i}...', end='')
print()




