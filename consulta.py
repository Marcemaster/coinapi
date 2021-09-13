import requests 

apikey = "D7D21BE0-283A-44D2-83BC-B8E0AE90247C"
url = 'https://rest.coinapi.io/v1/exchangerate/BTC/EUR?apikey=D7D21BE0-283A-44D2-83BC-B8E0AE90247C'


respuesta = requests.get(url)

print(respuesta.json()['rate'])