import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM é p dizer q é conexão UDP

print('Socket Criado com Sucesso!')

host = 'localhost'
porta = 5432

s.bind((host,porta)) #conexão entre Servidor e Cliente
mensagem = '\nServidor: Olá Cliente!'

while 1:
    dados, end = s.recvfrom(4096) #4096 é a qnt de bytes

    if dados:
        print("Servidor enviando mensagem...")
        s.sendto(dados + (mensagem.encode()), end)