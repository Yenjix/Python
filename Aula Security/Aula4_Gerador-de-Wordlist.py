import itertools

string = input('String a ser permutada')
resultado = itertools.permutations(string, len(string)) #('quais palavras', quantas permutações)

for i in resultado:
    print(''.join(i)) #O join junta os caracteres