from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento:'))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação:\033[1;31m Mirim\033[1;31m')
elif idade <= 14:
    print('Classificação:\033[1;32m Infantil\033[1;32m')
elif idade <= 19:
    print('Classificação:\033[1;34m Junior\033[1;34m')
elif idade <= 25:
    print('Classificação:\033[1;35m Sênior\033[1;35m')
else:
    print('Classificação:\033[1;36;m Master\033[1;36m')

