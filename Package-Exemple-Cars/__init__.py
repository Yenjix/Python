# Exemplo tirado de: https://www.geeksforgeeks.org/create-access-python-package/#:~:text=First%2C%20we%20create%20a%20directory,the%20directory%20is%20a%20package.
# 15/03/2022 20h39
from Bmw import Bmw
from Audi import Audi
from Nissan import Nissan

# Create an object of Bmw class & call its method
ModBMW = Bmw()
ModBMW.outModels()

# Create an object of Audi class & call its method
ModAudi = Audi()
ModAudi.outModels()

# Create an object of Nissan class & call its method
ModNissan = Nissan()
ModNissan.outModels()