import requests

def obtener_noticias(api_key, categoria):
    base_url = 'https://newsapi.org/v2/top-headlines'
    

    params = {
        'apiKey': api_key,
        'country': 'ar',  
        'category': categoria  
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        noticias = response.json()
        articles = noticias.get('articles', [])
        
        if articles:
            print(f"Se obtuvieron {len(articles)} noticias exitosamente.")
            return articles
        else:
            print('La respuesta de la API no contiene artículos.')
            return []
    else:
        print('Error al obtener noticias:', response.status_code)
        return []
