lista = [1,3,5,7]
lista_animal=['cachorro','gato','elefante']
print(lista)
print(lista_animal[1])

for x in lista_animal:
    print(x)

soma=0
for x in lista:
    print(x)
    soma+=x

print(soma)
print(sum(lista))
print(max(lista))
print(min(lista))
print(max(lista_animal))
print(min(lista_animal))

if 'gato' in lista_animal:
    print('existe um gato na lista')
else:
    print('não existe um gato na lista')
    lista_animal.append('lobo')
    print(lista_animal)

lista_animal.pop() #remove o ultimo elemento da lista, no caso o lobo
#da para escolher a posiçao tbm
print(lista_animal)

#se quiser remover um elemento que voce conhece: use o .remove
#lista_animal.remove('elefante')

nova_lista=lista_animal*3
print(nova_lista)

lista_animal=['cachorro','gato','elefante','lobo','arara']
#organizar por ordem numerica ou alfabetica
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

lista_animal.reverse()

#Diferença entre Lista e Tupla
#Lista é mutavel os valores, ou seja, a gente consegue alterar eles
#Já na Tuplas os valores não podem ser alterados
#Na tupla a gente usa parenteces
#comando tuple converte (?)

tupla=(1,10,12,14)
print(tupla[2])


print(len(tupla))
print(len(lista_animal))
print(type(tupla))
print(type(lista_animal))
