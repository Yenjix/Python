import ipaddress #ja é uma biblioteca padrao do Python 3

ip = '192.168.0.1'
endereco = ipaddress.ip_address(ip)

print(endereco)
print(endereco + 100)
print(endereco + 256)
print(endereco + 257)
print(endereco + 2000)

#Da para trabalhar com redes tbm
ip = '192.168.0.0/24' #tem q ser uma rede valida
#redes: /4 /24 /32 /0 ... Tem mais
rede = ipaddress.ip_network(ip)

print(rede)

for ip in rede: #imprimir todos os ip dentro da rede
    print(ip)