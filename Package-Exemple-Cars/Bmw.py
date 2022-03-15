# https://www.geeksforgeeks.org/create-access-python-package/#:~:text=First%2C%20we%20create%20a%20directory,the%20directory%20is%20a%20package.

class Bmw:
    def __init__(self):
        self.models = ['i8', 'x1', 'x5', 'x6']

    def outModels(self):
        print('These are the avilable models for BMW')
        for model in self.models:
            print('\t%s ' % model)
