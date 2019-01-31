preco=float(input('Digite o valor do produto:'))
desconto=((preco*5)/100)
final=preco-desconto
print('Na promoção fica {:.2f}R$, o valor inicial era de: {:.2f}R$.'.format(final,preco))
