#abrir arquivo
import shutil
def escrever_arquivo(texto):
open('teste.txt', 'w')
#diretorio = 'C:/pythonProject/teste.txt'
#arquivo = open(diretorio,'w')
#'a' da p ficar atualizando p proxima linha se tiver \n
arquivo.write('Minha primeira escrita')
arquivo.close()

def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open(nome_arquivo,'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo=open(nome_arquivo, 'r')
    texto=arquivo.read()
    print(texto)

def media_notas(nome_arquivo)
    arquivo = open(nome_arquivo,'r')
    aluno_nota=arquivo.read()
    print(aluno_nota)
    aluno_nota=aluno_nota.split('\n') #toda vez q ele encontra um ENTER ele vai dividir, virar um item da lista
    print(aluno_nota)
    for x in aluno_nota:
        #print(x) tem q transformar isso numa lista, assim ele ler como string, letra por letra
        lista_notas=x.split(',')
        print(lista_notas)
        aluno=lista_notas[0]
        lista_notas.pop(0) #vai tirar o nome do aluno q é string
        #agora a gente tem q converter para INTEIRO e fazer a SOMA
        media = lambda notas: sum([int(i) for i in notas])/4
        print(aluno)
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, "C:/pythoProject/notas_alunos.txt")

def move_arquivo(nome_arquivo):
    import shutil
    shutil.move(nome_arquivo, 'C:/pythoProject/')
if __name__ == '__main__':
    copia_arquivo('notas.txt')
    lista_media=media_notas('notas.txt')
    print(lista_media)
    #escrever_arquivo('Primeira linha.\n)
    aluno='Rafael,10,5,5,10\n'
    #aluno='Felipe,7,8,5,6\n
    #aluno=Galleani,7,8,5,6\n
    #aluno=Cesar,7,9,3,8\n
    #atualizar_arquivo('notas.txt,aluno)
    ler_arquivo('teste.txt')

