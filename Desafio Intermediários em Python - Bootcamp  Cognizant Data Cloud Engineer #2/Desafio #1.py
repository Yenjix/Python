# TODO: Complete os espaços em branco com uma solução possível para o problema.
counter = 0
for x in range(6):
    number = float(input("Digite um número: "))
    if number > 0:
        counter += 1

print("{} valores positivos".format(counter))