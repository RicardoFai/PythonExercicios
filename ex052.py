núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm+ 1):
    if núm % c == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n \033[34mO número {} foi divisível {} vezes'.format(núm, tot))
if tot == 2:
    print('\033[1;32m por isso ele É PRIMO!\033[1;32m')
else:
    print('\033[1;31mE por isso ele NÃO É PRIMO!\033[1;31m')