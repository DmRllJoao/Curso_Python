km=int(input('Digite a quantidade de km rodados:'))
dias=int(input('Quantidade de dias no qual ele foi alugado:')
)
dias_final=60*dias
km_final=km*0.15
final=dias_final+km_final
print('O total a pagar é de {:.2f}R$.'.format(final))
