import pytest
from etl.transform import clean_users_data, valid_email, concat_address
from typing import List, Dict

# Pruebas funciones auxuliares

def test_valid_email():
    """a validacion de correos electronicos"""
    assert valid_email("ejemplo@ejemplo.com") is True
    assert valid_email("Jondoe@domain.co.uk") is True
    assert valid_email("emailémail") is False
    assert valid_email("prueba@prueba") is False
    # Valores nulos
    assert valid_email(None) is False

def test_concat_address():
    """Prueba que la funcion concatene correctamente la diección"""
    address_data = {
        "street": "Kulas Light", 
        "suite": "Apt. 556", 
        "city": "Gwenborough", 
        "zipcode": "92998-3874"
    }
    expected_value = "Kulas Light, Apt. 556, Gwenborough, 92998-3874"
    assert concat_address(address_data) == expected_value

def test_concat_address_values_null():
    """Valida que la funcion concatene la direccion un si faltan datos"""
    address_data = {
        "street": "Kulas Light", 
        "suite": "Apt. 556",
    }
    expected_value = "Kulas Light, Apt. 556"
    assert concat_address(address_data) == expected_value

# Pruebas para la funcion principal

@pytest.fixture
def sample_data():
    """Fixture de Pytest para proveer de datos para las pruebas de la funcion principal"""
    return [
        # usuario valido
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
        # usurio con email invalido
        {
            "id": 2,
            "name": "Ervin Howell",
            "username": "Antonette",
            "email": "Shanna@melissa",
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
        },
        # usuario con id repetido
        {
            "id": 1,
            "name": "Clementine Bauch",
            "username": "Samantha",
            "email": "Nathan@yesenia.net",
            "address": {
            "street": "Douglas Extension",
            "suite": "Suite 847",
            "city": "McKenziehaven",
            "zipcode": "59590-4157",
            "geo": {
                "lat": "-68.6102",
                "lng": "-47.0653"
            }
            },
            "phone": "1-463-123-4447",
            "website": "ramiro.info",
            "company": {
            "name": "Romaguera-Jacobson",
            "catchPhrase": "Face to face bifurcated interface",
            "bs": "e-enable strategic applications"
            }
        },
        # usuario valido
        {
            "id": 4,
            "name": "Patricia Lebsack",
            "username": "Karianne",
            "email": "Julianne.OConner@kory.org",
            "address": {
            "street": "Hoeger Mall",
            "suite": "Apt. 692",
            "city": "South Elvis",
            "zipcode": "53919-4257",
            "geo": {
                "lat": "29.4572",
                "lng": "-164.2990"
            }
            },
            "phone": "493-170-9623 x156",
            "website": "kale.biz",
            "company": {
            "name": "Robel-Corkery",
            "catchPhrase": "Multi-tiered zero tolerance productivity",
            "bs": "transition cutting-edge web services"
            }
        }
    ]


def test_transform_flow(sample_data: List[Dict]):
    """Prueba completa del flujo del ETL"""

    transformed_data = clean_users_data(sample_data)

    # validar que el umero de registros que debe retornar sea el esperado
    assert len(transformed_data) == 2

    # Extraer datos del primer registro para validar
    user = transformed_data[0]

    assert user["id"] == 1
    assert user["name"] == "LEANNE GRAHAM"
    assert user["email"] == "Sincere@april.biz"
    assert user["full_address"] == "Kulas Light, Apt. 556, Gwenborough, 92998-3874"