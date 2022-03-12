
lista=[1,10]
try:
    arquivo = open('teste.txt', 'r')
    texto=arquivo.read
    divisao=10/0
    #numero = lista[3]
    #x = a

    #Se ligar que tem HIERARQUIA entre os Erros, sempre começar com os FILHOSD e por último
    #os PAIS, se não os PAIS vao absorver todos os erros.
    #Ele começa a ler os erros definidos de cima p baixo
    #Se colocar a BaseException primeiro, ele ja entra nele, nem executa os outros
except ZeroDivisionError:
    #ZeroDivisionError é uma classe de exceção que ja vem acoplada no python
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print("Houve um erro de aritmética")
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:
    #Todas as exceções tem PAI e FILHO
    #BaseException é o PAI de todas as exceções
    #Ele é a primeira das exceções, todas as exceções vem depois dela
    #Qlqr outro erro diferente de Zero e Index (q foram declaradas) vao cair aqui
    print('erro desconhecido. Erro: {}'.format(ex))
except:
    print("Erro desconhecido")
else:
    print('Executa quando não ocorre exceção(erro)')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
    #sempre fechar o arquivo aqui, pois o FINALLY é sempre executado

try:
    numero = lista[3]
except IndexError:
    print('Erro ao acessar um indice inválido da lista')