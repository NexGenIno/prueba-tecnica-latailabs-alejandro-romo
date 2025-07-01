import os
import csv
import pytest
from etl.load import load_users_to_csv


@pytest.fixture
def sample_data():
    """Fixture con data valida para escribir en el archivo de salida"""
    return [
        {
            "id": 1,
            "name": "LEANNE GRAHAM",
            "email": "Sincere@april.biz",
            "full_address": "Kulas Light, Apt. 556, Gwenborough, 92998-3874"
        },
        {
            "id": 2,
            "name": "ERVIN HOWELL",
            "email": "Shanna@melissa.tv",
            "full_address": "Victor Plains, Suite 879, Wisokyburgh, 90566-7771"
        }
    ]

def test_load_users_data_to_csv(sample_data, tmp_path):
    """Prueba que la fincion escribe correctamente el archivo csv"""

    # Defiir ruta temporal del archivo para no escribir dentro del directori
    output_file = tmp_path / "sample_output_file.csv"
    HEADERS = ["id", "name", "email", "full_address"]

    load_users_to_csv(sample_data, str(output_file), HEADERS)

    # verificar si se crea el archivo
    assert os.path.exists(output_file)

    # validar que exista contenido dentro del archivo
    with open(output_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        # Validar las cabceras del archivo
        assert rows[0] == ["id", "name", "email", "full_address"]

        # Contar el numero de filas que coinsidan con sample_data
        assert len(rows) -1 == len(sample_data)

        # Validar que el primer registro de sample_data coincida con el del temp_file
        assert rows[1] == ["1", "LEANNE GRAHAM", "Sincere@april.biz", "Kulas Light, Apt. 556, Gwenborough, 92998-3874"]