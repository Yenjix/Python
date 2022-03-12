for x in range(1,101):
    print(x)

#Verificar se o número digitado é primo:
a=int(input("Entre com um número: "))

div=0
for x in range(1,a+1):
    resto=a%x
    print(x, resto)
    if resto == 0:
        div=div+1
        #ou poderia ser div +=1

if div==2:
    print('número {} é primo.'.format(a))
else:
    print('número {} não é primo.'.format(a))


print('Verificar quais são os primos até um valor informado\nSerá um for dentro de outro for:"
    a=int(input("Entre com um número: "))

    for num in range(a+1)
        div=0
        for x in range(1,num+1):
            resto=num%x
            #print(x, resto)
            if resto == 0:
                div=div+1
                #ou poderia ser div +=1

        if div==2:
            print(num)


