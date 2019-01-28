import random
lista_aleatoria=[]
lista_usuario=[]
lista_final=[]
lista_organizada=[]
contador=int(1)
limite=int(13)
contador2=int(1)
acertos=int(0)
while contador<=limite:
  numero=int(random.randint(1, 100))
  lista_aleatoria.append(numero)
  contador=contador+1
numero_do_cartao=int(input('Digite o número do cartão:'))
print(lista_aleatoria)
while contador2<=limite:
  numeros_usuario=int(input('Digite os 13 números desejados de 1 até 100:'))
  lista_usuario.append(numeros_usuario)
  contador2=contador2+1
for x in lista_usuario:
  if x not in lista_final:
    lista_final.append(x)
while len(lista_final)!=limite:
  novamente=int(input('O sorteio não aceita números repetidos, e o seu cartão contém números repetidos, digite outro número que não seja igual por gentileza:'))
  while novamente in lista_usuario:
    novamente=int(input('Se repetiu, por favor digite outro número:'))
  lista_final.append(novamente)
for z in lista_aleatoria:
  if z in lista_final:
    acertos=acertos+1
    lista_organizada.append(z)
if lista_final==lista_aleatoria:
  print('O número do cartão é:{}, você acertou {} números, dentre deles foram os {}, o gabarito do sorteio é:{}, parabéns você o ganhador!!'.format(numero_do_cartao,acertos,lista_organizada,lista_aleatoria))
else:
  print('O número do cartão é:{}, você acertou {} números, dentre deles foram os {}, o gabarito do sorteio é:{}, você não é o ganhador,pois tem que acertar todos,tente novamente,boa sorte!!'.format(numero_do_cartao,acertos,lista_organizada,lista_aleatoria))
