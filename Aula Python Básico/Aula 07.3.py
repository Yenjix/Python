#outro jeito de fazer é sem o Self Definido, você precisa dar os valores para as funções

class Calculadora:

        def soma(self,valor_a,valor_b):
            return valor_a + valor_b

        def subtracao(self,valor_a,valor_b):
            return valor_a - valor_b

        def multiplicacao(self,valor_a,valor_b):
            return valor_a * valor_b

        def divisao(self,valor_a,valor_b):
            return valor_a / valor_b

print(Calculadora.soma(12,15))
print(Calculadora.subtracao(4,10))
print(Calculadora.multiplicacao(10,5))
print(Calculadora.divisao(30,2))