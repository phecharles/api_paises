import sys

import requests
import json

URL_ALL = "https://restcountries.com/v2/all"
URL_NAME = "https://restcountries.com/v2/name"

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

def mostrar_populacao(nome_pais):
    resposta = requisicao("{}/{}".format(URL_NAME, nome_pais))
    if resposta:
        lista_paises = parsing(resposta)
        if lista_paises:
            for pais in lista_paises:
                print("População do {}: {}".format(pais['name'], pais['population']))
    else:
        print("País não encontrado!")

def mostrar_moedas(nome_pais):
    resposta = requisicao("{}/{}".format(URL_NAME, nome_pais))
    if resposta:
        lista_paises = parsing(resposta)
        if lista_paises:
            for pais in lista_paises:
                print("Moedas do {}".format(pais['name']))
                moedas = pais['currencies']
                for moeda in moedas:
                    print(moeda)
    else:
        print("País não encontrado!")


if __name__ == "__main__":
    # mostrar_populacao("brazil")
    # mostrar_moedas("brazil")

    print(sys.argv)

