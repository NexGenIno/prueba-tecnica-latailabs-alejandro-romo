import logging
import os
from etl.extract import extract_users
from etl.transform import clean_users_data
from etl.load import load_users_to_csv


# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="etl_process.log"
)

# Definiciones
API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_DIR = "output"
OUTPUT_FILENAME = "users_cleaned.csv"
OUTPUT_FILEPATH = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)
HEADERS = ["id", "name", "email", "full_address"]

def run_etl():
    """
    Ejecuta el proceso ETL completo
    """

    logging.info("Iniciando proceso ETL...")

    # Extraer
    logging.info(f"Extracción de datos desde: {API_URL}")

    users_data = extract_users(API_URL)

    if not users_data:
        logging.error("No se extajeron datos terminado el proceso ETL,,,")
        return
    
    logging.info(f"-> {len(users_data)} registros extraidos.")

    # Transformar
    transformed_users = clean_users_data(users_data)
    logging.info(f"-> {len(transformed_users)} Registros despues de la transformacion de datos")

    # Cargar
    load_users_to_csv(transformed_users, OUTPUT_FILEPATH, HEADERS)
    logging.info("Proceso ETL terminado")


if __name__ == "__main__":
    run_etl()
