import random, string

tamanho = int(input('Digite o tamanho de senha que você deseja: '))
chars = string.ascii_letters + string.digits + '!@#$%&*()-=+,.;:/?'
rnd = random.SystemRandom() #os.urandom ela gera numeros randoms fornecidos pelo OS

print('='*60)
print('Senha Gerada:')
print(''.join(rnd.choice(chars) for i  in range(tamanho)))
print('='*60)