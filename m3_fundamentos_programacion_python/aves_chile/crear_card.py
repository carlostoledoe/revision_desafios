def crear_card(datos):
    cards = ''
    for dato in datos:
        cards += f'''
    <div class="card" style="width: 18rem;">
        <img src="{dato['images']['thumb']}" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">{dato['name']['spanish']}</h5>
            <p class="card-text">Este es el texto estandar para todas las card</p>
        </div>
        <ul class="list-group list-group-flush">
            <li class="list-group-item">Nombre en Ingles: {dato['name']['english']}</li>
        </ul>
    </div>
    
    '''
    return cards