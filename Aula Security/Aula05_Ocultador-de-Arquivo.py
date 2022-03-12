#Você consegue ocultar arquivo ou pasta
#testando com o arquivo txt: Aula05_Ocultar.txt

import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('Aula05_ocultar.txt', atributo_ocultar)

if retorno:
    print('Arquivo ocultado')
else:
    print('Arquivo não ocultado')

#pasta = input("Digite o caminho da pasta a ser ocultado ex: C:/pasta: ")
#retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)
#if retorno:
#    print('Pasta ocultado')
#else:
#   print('Pasta não ocultado')