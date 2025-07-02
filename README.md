# Proyecto ETL - Prueba Técnica - LataiLabs

Este proyecto implementa un flujo ETL (Extract, Transform, Load) completo en python. El proceso extrae datos de usuarios desde API pública, los valida, limpia y transorma y finalmente los carga a un archivo CSV.

El diseño del proyecto se basa en los requerimientos de la prueba técnica, siguiendo las mejores prácticas en la industria, incluye validación con Pydatic, purbas unitarias con Pytest y un sistema de logging para monitore.

### Características Principales

-   Extracción: Obtiene datos de usuarios desde una API REST externa usando `requests`.
-   Validación: Utiliza `Pydantic` para validar la estructura y los tipos de datos en la frontera del sistema, garantizando la integridad de los datos antes del procesamiento.
-   Transformación: Aplica reglas de negocio claras para limpiar y normalizar los registros (mayúsculas, direcciones unificadas, eliminación de duplicados).
-   Carga: Guarda los datos procesados en un archivo `.csv` limpio y listo para su uso.
-   Testing: Cobertura de pruebas unitarias con `pytest` para asegurar el correcto funcionamiento de la lógica de transformación y carga.
-   Logging: Registro detallado de eventos, advertencias y errores en un archivo `etl_process.log` para facilitar la depuración y el monitoreo del proceso.

### Estructura del Proyecto

etl_users_project/
├── etl/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── models.py
├── tests/
│   ├── __init__.py
│   ├── test_transform.py
│   └── test_load.py
├── output/
│   └── users_cleaned.csv
├── etl_process.log
├── main.py
├── requirements.txt
└── README.md

### Instalación y Ejecución

Sigue estos pasos para poner en marcha el proyecto. Se recomienda usar un entorno virtual.

#### 1. Preparar el Entorno

```bash
# Clona este repositorio o descarga los archivos
# git clone https://github.com/NexGenIno/prueba-tecnica-latailabs-alejandro-romo.git
# cd etl_users_project

# Crea un entorno virtual
python -m venv venv

# Activa el entorno virtual
# En Windows:
# venv\Scripts\activate
# En macOS/Linux:
# source venv/bin/activate
```

#### 2. Instalar Dependencias
Una vez activado el entorno virtual, instala las librerías necesarias.
```bash
pip install -r requirements.txt
```

#### 3. Ejecutar el Proceso ETL
Para correr el pipeline completo, ejecuta el script principal:
```bash
python main.py
```
Esto contactará la API, procesará los datos y creará el archivo `output/users_cleaned.csv`.

#### 4. Ejecutar las Pruebas
Para verificar que todos los componentes funcionan correctamente, ejecuta `pytest`:
```bash
pytest
```
### Archivo de Log

El proceso genera un archivo `etl_process.log` en la raíz del proyecto. Este archivo contiene un registro detallado de cada paso de la ejecución, incluyendo información, advertencias y errores, lo que facilita el seguimiento de la actividad del pipeline.