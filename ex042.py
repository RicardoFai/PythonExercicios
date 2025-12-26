r1 = float(input('Primenro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if r1 == r2 == r3:
        print('\33[1;30mEQUILÁTERO\33[1;30m')
    elif r1 != r2 != r3 != r1:
            print('\33[;31mESCALENO\33[;31m')
    else:
        print('\033[;32mISÓCELES\033[;32m')
else:
    print('\033[;34mOs segmentos acima NÃO PODEM FORMAR um triângulo!\033[;34m ')