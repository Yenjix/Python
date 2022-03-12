from bs4 import BeautifulSoup #Biblioteta para extraçao de dados em HTML ou XML
#foi necessario instalar a biblioteca bs4
#clica em: File>Settings... >Projectpython > Python Interpreter > clica no simbolo do + (para add) > procura o nome da biblioeteca > OK
#https://www.youtube.com/watch?v=HJ9bTO5yYw0&ab_channel=Ninenox

import requests

site = requests.get('https://www.climatempo.com.br/').content #vai pegar everthing do html, recebendo o conteudo da requisição http do site
soup = BeautifulSoup(site, 'html.parser') #objeto soup baixa o site, o html

print(soup.prettify()) #transforma o html em string

#temperatura = soup.find('span', class_='_block _margin-b-5 -gray')#tem q colocar esse _ depois do class p evitar erro
#print(temperatura.string)
print(soup.title.string)
print(soup.a) #ou print(soup.a.string) p tirar os <a </a>
print(soup.p.string)
print(soup.find('admin'))

