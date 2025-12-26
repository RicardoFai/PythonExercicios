'''distância = float(input('Qual é a distância da sua viagem?'))
print('Você está preste a começar sua viagem de {}Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da passagem será de R${:.2f}'.format(preço))'''


distância = float(input('Qual é a distância de sua viagem?'))
print('Você esá presete a começar sua viagem de {}Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da passagem será de R${:.2f}'.format(preço))