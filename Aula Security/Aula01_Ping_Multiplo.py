import os
import time #vamos adicionar um tempo de espera, qnd for imprimir os pings

with open('Aula01_host.txt') as file:
    dump = file.read()
    dump = dump.splitlines() #ele vai pular só qnd encontrar \n

    for ip in dump:
        print('Verificando o ip: ', ip)
        print('-'*60)
        os.system('ping -n 2 {}'.format(ip))
        print('-'*60)
        time.sleep(5)#5s para mandar um proximo ping