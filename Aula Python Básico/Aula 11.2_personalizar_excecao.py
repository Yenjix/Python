#Transformar toda nota de aluno >10 e <0 em exceção
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self,message):
        self.message=message

while True:
    try:
        x=input('Entre com uma nota de 0 a 10: ')
        print(x)
        if x>10:
            raise InputError('Nota não pode ser maior que 10') #forçando uma Exceção
        elif x<0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)

