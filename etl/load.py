import csv
import os
from typing import List, Dict


def load_users_to_csv(data: List[Dict], output_file_path: str, fields_names: List[str]) -> None:
    """

    Carga los datos de los usuarios transformados a un archivo .csv

    Args:
        data(List[Dict]): Lista con los usuarios ya procesados.
        output_file_path(str): Ruta completa del archivo de salida.
        fields_names(List[str]): Lista de str con los nombres del los encabezados del archivo.
    """

    output_dir = output_file_path

    # Crear el directorio en caso de no existir
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        with open(output_file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields_names)
            writer.writeheader()
            writer.writerows(data)
    except IOError as e:
        print(f"Error al escribir csv: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    # Ejemplo para prueba manual
    transformed_users = [
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

    OUTPUT_FILE = "output/users_cleaned.csv"
    HEADERS = ["id", "name", "email", "full_address"]

    load_users_to_csv(transformed_users, OUTPUT_FILE, HEADERS)

    # Verificación de archivo solo para desarrollo
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print(f"primeras líneas del archivo: \n" + "".join(lines[:2]))
    else:
        print(f"Error no se encontro el archivo: {OUTPUT_FILE}")
