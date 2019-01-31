salario=float(input('Digite o valor do produto:'))
desconto=((salario*15)/100)
final=salario+desconto
print('Com reajuste salarial seu salário fica em: {:.2f}R$, o salário era de: {:.2f}R$.'.format(final,salario))
