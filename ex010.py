real = float(input('Quanto de dinheiro voce tem na carteira? R$'))
dolar = real / 5.56
euro = real / 6.45
print('Com R${:.2f} voce pode comprar US${:.2f} e tambem o Eur{:.2f }'.format(real,dolar,euro))