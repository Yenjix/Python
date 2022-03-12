import os #Importa o módulo ou biblioteca os (integra os programas e
#recursos do S.O.

print('#'*60) ##Imprime #60 vezes
ip_ou_host = input('Digite o Ip ou host a ser verificado: ')
#O DNS do google é 8.8.8.8; é DNS mesmo?
#pode digita www.google.com  tbm
print("-"*60)

os.system('ping -n 6 {}'.format(ip_ou_host)) #-n -num de pacotes que no caso são 6



