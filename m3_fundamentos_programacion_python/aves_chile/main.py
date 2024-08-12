from consulta import request_get
from crear_card import crear_card
from crear_html import crear_html
from crear_archivo import crear_archivo


url = 'https://aves.ninjas.cl/api/birds'

datos_pajaros = request_get(url)

cards = crear_card(datos_pajaros)

plantilla = crear_html(cards)



crear_archivo(plantilla)