#import Aula7
from Aula 7.4 import Televisao
from Aula 7.2 import Calculadora

#if __name__ == '__main__':
televisao = Televisao
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
calculadora = Calculadora(5,10)
print(calculadora.soma())

