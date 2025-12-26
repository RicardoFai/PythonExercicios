from datetime import date
atual = date.today().year
H == 1
M == 2
int(input('Qual é o seu gênero?'.format(H, M)
if gênero == H:
    nasceu =  int(input())
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para  o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos. '.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
elif gênero == 2:
     print('Você é Mulher, portanto não tem a obrigação de se alistar!')

