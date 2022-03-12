import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente Socket criado com Sucesso!')

host = 'localhost' #vai receber o IP Local de Rede do PC
porta = 5433 #Defimos a porta
mensagem = 'Olá servidor!'

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))#empacota a msg e manda pro servidor
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("Cliente: " + dados)
finally:
    print('Cliente: Fechando a Conexão.')
    s.close() #fechar a conexão para não ficar em loop.

#Tem q rodar ele e o Aula02_ServidorUDP juntos para funcionar