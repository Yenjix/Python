#Paralelismo; programa vai conseguir enviar e receber pacotes ao mesmo tempo através dos threads
#Jogo de corrida, dois carrinhos vao disputar entre si, uma corrida com uma determina kilometragem, pórem
#com velocidades diferentes
import time

#def carro1(velocidade):
#   trajeto = 0 #kilometro zero
#    while trajeto <= 100:
#        print('Carro1: ', trajeto)
#        trajeto +=velocidade
#        time.sleep(0.5)

#def carro2(velocidade):
#    trajeto = 0 #kilometro zero
#    while trajeto <= 100:
#        print('Carro2: ', trajeto)
#        trajeto +=velocidade

#carro1(10)
#carro2(20)
#desse jeito ta correndo 1x por vez

from threading import Thread #da biblioteca threading importar a classe Thread (vai fazer correr simultaneamente)
def carro(velocidade, piloto):
    trajeto = 0 #kilometro zero
    while trajeto <= 100:
        print('Piloto: {} km: {} \n'.format(piloto, trajeto))
        trajeto +=velocidade
        time.sleep(0.5)

t_carro1 = Thread(target=carro, args=[1, 'Bruno']) #args seria a "velocidade"
t_carro2 = Thread(target=carro, args=[1.5, 'Pedro'])

t_carro1.start()
t_carro2.start()