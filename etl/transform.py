import logging
from typing import List, Dict
from .models import User, Address


# instancia especifica de logging para el modulo
logger = logging.getLogger(__name__)



def concat_address(data_address: Address) -> str:
    """

    Une los campos street, suite, city y zipcode en un solo str

    Args:
        data_address(Dict): Diccionario con los datos de la dirección.

    Returns:
        str: Dirección separada por comas.
    """

    parts = [data_address.street, data_address.suite, data_address.city, data_address.zipcode]
    return ", ".join(part for part in parts if part)

def clean_users_data(users: List[User]) -> List[Dict]:
    """

    Aplica transformación a los datos de usuario según reglas de negocio.

    Args:
        users(List[Dict]): Lista de usuarios extraidos desde la API.

    Resturns:
        List[Dict]: Lista de usuarios transformados.
    """

    transformed_users: List[Dict] = []
    completed_ids: set = set() # Conjunto para evitar IDs duplicados

    for user in users:
        

        if user.id is None or user.id in completed_ids:
            logger.warning(f"Usuario con id: {user.id} duplicado")
            continue

        completed_ids.add(user.id)

        transformed_users.append({
            "id": user.id,
            "name": user.name.upper(),
            "email": user.email,
            "full_address": concat_address(user.address)
        })
    
    logger.info(f"Transformacion de datos exitosa, total de registrs: {len(transformed_users)}")
    return transformed_users


if __name__ == "__main__":
    # Datos de prueba
    users = [
        {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
            }
        },
        {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
            }
        },
        {
            "id": 2,
            "name": "Ervin Howell",
            "username": "Antonette",
            "email": "Shanna@melissa.tv",
            "address": {
            "street": "Victor Plains",
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771",
            "geo": {
                "lat": "-43.9509",
                "lng": "-34.4618"
            }
            },
            "phone": "010-692-6593 x09125",
            "website": "anastasia.net",
            "company": {
            "name": "Deckow-Crist",
            "catchPhrase": "Proactive didactic contingency",
            "bs": "synergize scalable supply-chains"
            }
        }
    ]

    transformed = clean_users_data(users)

    import json
    logger.info(json.dumps(transformed, indent=2))

    assert len(transformed) == 2 # Validar que solo tienen que ser 2 registros
