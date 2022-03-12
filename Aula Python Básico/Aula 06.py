#Conjuntos você define usando chaves: {}
#Os conjuntos nao tem duplicidade, ele só ler os elementos iguais 1x
conjunto = {1,2,3,4,4,2}
print(conjunto)
conjunto.add(5)
print(conjunto)
conjunto.discard(2)
print(conjunto)

conjunto1={1,2,3,4,5}
conjunto2={5,6,7,8}
conjunto_uniao=conjunto1.union(conjunto2)
print(conjunto_uniao)
conjunto_interseccao=conjunto1.intersection(conjunto2)
print(conjunto_interseccao)
conjunto_diferenca1=conjunto1.difference(conjunto2)
conjunto_diferenca2=conjunto2.difference(conjunto1)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print("Diferença entre 2 e 1: {}".format(conjunto_diferenca2))
conjunto_diff_simetrica=conjunto1.symmetric_difference(conjunto_diferenca2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_a={1,2,3}
conjunto_b={1,2,3,4,5}
conjunto_subset=conjunto_b.issubset(conjunto_a)
print('A é subconjunto de B: {}'.format(conjunto_subset))
conjunto_superset=conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}',format(conjunto_superset))

#Converter uma Lista para Conjunto
lista=['cachorro','cachorro','gato','gato','elefante']
print(lista)
conjunto_animais=set(list)
print(conjunto_animais)
lista_animais=list(conjunto_animais)
print(lista_animais)