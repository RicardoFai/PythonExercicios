num = int(input('\033[1;34mDigite um número inteiro:\033[1;34m'))
print('''\033[1;35mEscolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL\033[1;35m''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a \033[1;31m{}\033[1;31m'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido oara OCTAL é igual a \033[1;30m{}\033[1;30m'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a \033[1;33m{}\033[1;33m'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
