import requests 

apikey = "D7D21BE0-283A-44D2-83BC-B8E0AE90247C"
url = 'https://rest.coinapi.io/v1/exchangerate/{}/{}'
cabecera = {"X-CoinAPI-Key": apikey}

mas = 's'

while mas == 's':
    de = input("Moneda de origen: ")
    a = input("Moneda de destino: ")

    respuesta = requests.get(url.format(de, a), headers=cabecera)
    if respuesta.status_code == 200:
        print(respuesta.json()['rate'])
    else:
        print(respuesta.status_code)
        print(respuesta.json())

    seguir = input("¿Quieres más (S/N)?:  ").lower()