import requests
from typing import List, Dict


def extract_users(url: str) -> List[Dict]:
    """

    Extrae datos de usuarios desde API pública.

    Args:
        url (str): URL de la API pública
    
    Returns:
        List[Dict]: Lista de diccionarios, cada uno representando un usuario.
        En caso de error, retorna una lista vacía.
    """

    try:
        response = requests.get(url)
        response.raise_for_status() # Cachar error de status en la peticion al api

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al intentar descargar la información: {e}")
        return []
    

if __name__ == "__main__":
    URL_API = "https://jsonplaceholder.typicode.com/users"
    data_users = extract_users(URL_API)

    if data_users:
        print(f"Se encontraron: {len(data_users)} usuarios")
    else:
        print("No se pudieron descagar datos desde la API")