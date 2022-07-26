import requests

URL = "https://restcountries.com/v2/all"
resposta = requests.get(URL)


print(resposta.text)