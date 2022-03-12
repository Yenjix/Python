#!! https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command
#Lembrar de verificar se o caminho do PIP ta correto
#
#You need to add the path of your pip installation to your PATH system variable. By default, pip is installed to C:\Python34\Scripts\pip (pip now comes bundled with new versions of python), so the path "C:\Python34\Scripts" needs to be added to your PATH variable.

#To check if it is already in your PATH variable, type echo %PATH% at the CMD prompt

#To add the path of your pip installation to your PATH variable, you can use the Control Panel or the setx command. For example:

#setx PATH "%PATH%;C:\Python34\Scripts"

#no meu caso: setx PATH "%PATH;C:\Users\Pedro\AppData\Local\Programs\Python\Python38\Scripts"
#Agora pode rodar os passos abaixos!



#CLica em 'External Libraries' na esqueda, pasta debaixo do Project.
#clica em python->site-packages 'são os pacotes instalados'
#o pip permite voce instalar outros pacotes
#Pode ir no PowerShell e digitar: pip --version ou no terminal do PyCharm
#comando: pip --help
#pip list : vai mostrar os pacotes instalados
#pip install requests -> esse pacote tem dependecias(ele vai instalar outras coisas)
#pip freeze -> p ver os pacotes instalados

#Instala o REQUESTS, vai no terminal e digita: pip install requests
#Só precisa instalar uma vez

import requests
#Formato JSON é um formato, traz informaçoes de dicionarii (?)
#Esse site é um API
def retorna_dados(cep)
    response = requests.get('https://viacep.com.br/ws/01001000/json/')
    print(response.status_code)
    print(response.text)
    print(response.json())
    dados_cep=response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    #API do pokemon
    response=requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_site(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    dados_pokemon = retorna_dados_pokemon('pikachu')
    print(dados_pokemon)
    print(dados_pokemon['sprites']['front_shiny'])
    receber_site=retorna_site('https://globallabs.academy/')
    print(receber_site)
    #Ele vai imprimir todo o HTML do site