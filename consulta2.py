from criptovalue import CriptoValueModel

modelo = CriptoValueModel()

seguir = "s"

while seguir == "s":
    de = input("Moneda de origen: ")
    a = input("Moneda de destino: ")

    modelo.de = de
    modelo.a = a 

    modelo.obtener()

