## Biblioteca re - Permite operações com expressões regulares
## Biblioteca json - Fornece operações de codificação e decodificação JSON
## urlib.request import urlopen - Funções e classes que ajudam a abrir URLs
## http://ipinfo.io/json

import re
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'
reposta = urlopen(url)
dados = json.load(reposta)
ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP externo\n')
print('IP: {4}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrg.: {0}'.format(org,regiao,pais,cid,ip))