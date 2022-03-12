import hashlib
#temos q criar dois arquivos e comparar eles:
#vou criar Aula3_CdH_A.txt e Aula3_CdH_B.txt


arquivo1 = 'Aula3_CdH_A.txt'
arquivo2 = 'Aula3_CdH_B.txt'

#Para o Hash ler os arquivos eles tem q ser lidos em BINARIO

hash1 = hashlib.new('ripemd160') #estamos dizendo qual o Algoritmo de Hash iremos utilizar, no caso: ripmd160
hash1.update(open(arquivo1, 'rb').read()) #.update vai comparar o Hash ;r de read e b de binario

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest(): #.digest ela resume os dados passados ao .update; ele cria outro hash do hash
    print(f'o arquivo: {arquivo1} é DIFERENTE do arquivo {arquivo2}') #esse f antes do '' é um .format diferente (?)
    print(f'O hash do arquivo: {arquivo1} é:', hash1.hexdigest())
    print(f'O hash do arquivo: {arquivo2} é:', hash2.hexdigest())
else:
    print(f'O arquivo: {arquivo1} é IGUAL ao arquivo: {arquivo2}')
    print(f'O hash do arquivo: {arquivo1} é:', hash1.hexdigest())
    print(f'O hash do arquivo: {arquivo2} é:', hash2.hexdigest())