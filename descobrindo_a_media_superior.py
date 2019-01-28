from functools import reduce
contador=1
lista_A=[]
lista_vazia=[]
while contador==1:
  n1=int(input('Digite os  números desejados:'))
  lista_A.append(n1)
  sair=int(input('Digite 1 para continuar ou 0 para sair:'))
  if sair==1:
    contador=contador+0
  else:
    contador=contador+1
produto_total = reduce(lambda x, y: x + y, lista_A)
final=float(produto_total/len(lista_A))
print('='*30)
print('A média deu:{}'.format(final))
print('='*30)
for x in lista_A:
  if x > final:
    lista_vazia.append(x)
bonito=(''.join(map(str, lista_vazia)))
print('Os números superiores a média são:{}'.format(bonito))
