import requests
import json

URL_ALL = "https://restcountries.com/v2/all"
URL_NAME = "https://restcountries.com/v2/name/brazil"

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except Exception as error:
        print("Erro ao fazer requisição", url)
        print(error)

def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        print("Erro ao fazer parsing")

def contagem(lista_de_paises):
    print(len(lista_de_paises))

def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])


if __name__ == "__main__":
    texto_da_resposta = requisicao(URL_ALL)
    if texto_da_resposta:
        lista_paises = parsing(texto_da_resposta)
        if lista_paises:
            contagem(lista_paises)
            listar_paises(lista_paises)


