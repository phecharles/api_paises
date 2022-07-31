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

def contagem():
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_paises = parsing(resposta)
        if lista_paises:
            return len(lista_paises)

def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])

def mostrar_populacao(nome_pais):
    resposta = requisicao("{}/{}".format(URL_NAME, nome_pais))
    if resposta:
        lista_paises = parsing(resposta)
        if lista_paises:
            for pais in lista_paises:
                print("População do {}: {} habitantes".format(pais['name'], pais['population']))
    else:
        print("País não encontrado!")

def mostrar_moedas(nome_pais):
    resposta = requisicao("{}/{}".format(URL_NAME, nome_pais))
    if resposta:
        lista_paises = parsing(resposta)
        if lista_paises:
            for pais in lista_paises:
                print("Moedas do", pais['name'])
                moedas = pais['currencies']
                for moeda in moedas:
                    print("{} - {} - {}".format(moeda['name'], moeda['code'], moeda['symbol']))
    else:
        print("País não encontrado!")

def ler_nome_do_pais():
    try:
        nome_do_pais = sys.argv[2]
        return nome_do_pais
    except:
        print("País não encontrado")



if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("## Bem vindo ao sistema de países ##")
        print("Uso: python paises.py <ação> <nome do país>")
        print("Ações disponíveis: contagem, moeda, populacao")
    else:
        argumento1 = sys.argv[1]

        if argumento1 == "contagem":
            numero_de_paises = contagem()
            print("Existem {} países em todo mundo.".format(numero_de_paises))
        elif argumento1 == "moeda":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_moedas(pais)
        elif argumento1 == "populacao":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print("Argumento inválido")





