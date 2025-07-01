import re
from typing import List, Dict


regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def valid_email(email: str) -> bool:
    """

    Comprobar si un email es válido usando un regex.

    Args:
        email (str): email a validar.
    
    Returns:
        bool: true si email es válido, false en caso contrario.
    """
    if not email:
        return False
    
    return bool(regex.match(email))

def concat_address(data_address: Dict) -> str:
    """

    Une los campos street, suite, city y zipcode en un solo str

    Args:
        data_address(Dict): Diccionario con los datos de la dirección.

    Returns:
        str: Dirección separada por comas.
    """

    street = data_address.get("street", "")
    suite = data_address.get("suite", "")
    city = data_address.get("city", "")
    zipcode = data_address.get("zipcode", "")

    clean_address_data = [segment for segment in [street, suite, city, zipcode] if segment]
    return ", ".join(clean_address_data)

def clean_users_data(users: List[Dict]) -> List[Dict]:
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
        user_id = user.get("id")
        name = user.get("name")
        email = user.get("email")
        address = user.get("address", {})

        if user_id is None or user_id in completed_ids:
            continue

        if not valid_email(email):
            continue

        completed_ids.add(user_id)

        uppercase_name = str(name).upper() if name else ""

        full_address = concat_address(address)

        transformed_users.append({
            "id": user_id,
            "name": uppercase_name,
            "email": email,
            "full_address": full_address
        })
    
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
    print(json.dumps(transformed, indent=2))

    assert len(transformed) == 2 # Validar que solo tienen que ser 2 registros
