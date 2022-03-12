a=int(input('Primeiro valor: '))
b=int(input('Segundo Valor: '))
c=int(input('Terceiro valor: '))

if a>b and a>c:
    print('o maior valor é {}'.format(a))
elif b>a and b>c:
    print('o maior número é {}'.format(b))
else:
    print('o maior número é {}'.format(c))
    print('final do programa')
