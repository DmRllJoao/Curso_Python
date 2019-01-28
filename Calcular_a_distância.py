distancia=int(input('Digite a distância em Km da sua viagem, e calcularei o preço:'))
if distancia<=200:
  preco=distancia*0.50
  print('A distância informada foi {} KM e lhe custará: {} reais!, sem desconto.'.format(distancia,preco))
else:
  preco2=distancia*0.45
  print('A distância informada foi {} KM e lhe custará: {} reais!, com desconto'.format(distancia,preco2))
