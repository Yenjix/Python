#TODO: Complete os espaços em branco com uma possível solução para o problema.
X, Y = map(int, input().split())
while (X != Y):
    floor = min(X, Y)
    top = max(X, Y)
    if (floor == X):
        print("Crescente")
    else:
        print("Decrescente")
    X, Y = map(int, input().split())