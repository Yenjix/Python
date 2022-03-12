segundos = int(input())

minutos = int(segundos/60) #
segundos = int(segundos - (minutos * 60))
horas = int(segundos/3600)#
minutos = int(minutos - (horas * 60))

print("{}:{}:{}".format(horas, minutos, segundos))