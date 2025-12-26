n1 = int(input('Primero número:'))
n2 = int(input('Segundo número:'))
if n1 > n2 :
    print('\033[4;36mO PRIMEIRO valor é maior\033[4;36m')
elif n2 > n1:
    print('\033[4;33mO SEGUNDO valor é maior\033[4;33m')
#elif n1 == n2:
    #print('\033[4;35mOs dois valores são IGUAIS\033[4;35m ')
else:
    print('\033[4;35mOs dois valores sã IGUAIS\033[4;35m')