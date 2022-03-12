import socket #relacionamento com a placa de rede, abertura e fechamento das portas
import sys #fornece a acesso à algumas variaveis e funções, que tem forte interação com o python

def main():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    except socket.error as e:
        print('A conexão falhou!')
        print("Erro: {}".format(e))
        sys.exit() #vai fechar o programa

    print('Socket criado com sucesso')

    HostAlvo = input('Digite o Host ou Ip a ser conectado: ')
    PortaAlvo = input('Digite a Porta a ser conectada: ')

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print('Cliente TCP conectado com Sucesso no Host: ' + HostAlvo + "e Porta: " + PortaAlvo)
        s.shutdown(2)#Vai esperar 2 segundo e fecha essa conecção para nao ficar em Loop
    except socket.error as e:
        print("Não foi possível conectar o Host: "+HostAlvo+' - Porta: '+PortaAlvo)
        print('Erro: {}'.format(e))
        sys.exit()

if __name__ == '__main__':
    main()