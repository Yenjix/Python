a=int(input('Entre com um valor: '))
resto=a%2
if resto ==0:
    print('número é par')
else:
    print('número é impar')

a=int(input('Entre com o primeiro valor: '))
b=int(input('Entre com o segundo valor: '))

resto_a=a%2
resto_b=b%2
if resto_a==0 or not resto_b>0:
    print('os dois numeros são pares')
else:
    print('pelo menos um número não é par')

a=int(input('Nota do Primeiro bimestre: '))
if a>10:
    a=int(input("Você digitou errado.\nDigite novamente a Nota do Primeiro bimestre: ")

b=int(input('Nota do Segundo bimestre: '))
    if b > 10:
        b = int(input("Você digitou errado.\nDigite novamente a Nota do Segundo bimestre: ")
c=int(input('Nota do Terceiro bimestre: '))
    if c > 10:
        c = int(input("Você digitou errado.\nDigite novamente a Nota do Terceiro bimestre: ")
d=int(input('Nota do Quarto bimestre: '))
if d>10:
    d=int(input("Você digitou errado.\nDigite novamente a Nota do Quarto bimestre: ")
media=(a+b+c+d)/4
print('média: {}'.format(media))
# if a<=10 and b<=10 and c<=10 and d<=10:
#     media=(a+b+c+d)/4
#     print('media: {}'.format(media))
# else:
#     print("foi informada alguma nota errada.")