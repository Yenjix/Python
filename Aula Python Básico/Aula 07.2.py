#Deifinianndo uma classe
class Calculadora:
    def __init__(self,numb1,numb2):
        self.valor_a = numb1
        self.valor_b = numb2

    def soma(self):
            return  self.valor_a + self.valor_b

    def subtracao(self):
            return  self.valor_a - self.valor_b

    def multiplicacao(self):
            return  self.valor_a * self.valor_b

    def divisao(self):
            return  self.valor_a / self.valor_b

if __name__ == '__main__':
teste=Calculadora(10,2)
print(teste.valor_a)
print(teste.valor_b)
print(teste.soma())
print(teste.subtracao())
print(teste.multiplicacao())
print(teste.divisao())
