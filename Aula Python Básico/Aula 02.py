a = 10
b = 5
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(type(soma))
soma = str(soma)
print('soma: ' + soma)
print('subtracação: ' + str(subtracao))
print('multiplicação: ' + str(multiplicacao))
print('divisão: '+str(divisao))
print('resto: '+str(resto))

a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))

print('soma: {}' .format(soma))
print('Soma: {}. Subtração: {}'.format(soma,subtracao))
#ou pode fazer isso
print('Soma: {soma}. \nSubtração: {subtracao}.'
      '\nMultiplicação: {multiplicacao}'
      '\nDivisão: {divisao}'
      '\nResto: {resto}'.format(soma=soma,
                                subtracao=subtracao,
                                multiplicacao=multiplicacao,
                                divisao=divisao,
                                resto=resto))

#print('soma: ' + str(soma))

# linha commentate
