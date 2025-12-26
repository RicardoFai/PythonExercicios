from random import randint
from time import sleep
Computador = randint(0,5) #Faz o computador pensar
#print('Pensei no número {}'.format(Computador))
print('-=-' *20)
print('Vou pensar em um número 0 e 5. Tente adivinhar...')
print('-=-' *20)
Jogador = int(input('Em que número pensei?')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if Jogador == Computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(Computador, Jogador))
