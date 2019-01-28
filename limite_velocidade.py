limite=int(input('Digite a velocidade do carro:'))
if limite>80:
  x=limite-80
  y=x*7
  print('você foi multado e terá que pagar o valor de: {} reias!'.format(y))
else:
  print('Você não foi multado')
print('Fim do programa')
