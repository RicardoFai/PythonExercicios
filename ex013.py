salário = float(input('Qual é o novo salário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento ele vai receber R${:.2f}'.format(salário, novo))