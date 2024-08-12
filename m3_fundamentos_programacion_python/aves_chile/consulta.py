import requests
import json

# Esta función entrega todos los datos de la API para ser manejados en un diccionario
def request_get(url):
    response = requests.get(url)
    datos = json.loads(response.text) # Tranforma en diccionario para iterar
    return datos