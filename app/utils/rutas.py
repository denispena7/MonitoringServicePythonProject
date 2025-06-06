import os

# Detecta la carpeta raíz del proyecto sin importar desde dónde se ejecute
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

def ruta_json(nombre_archivo):
    return os.path.join(BASE_DIR, 'config', nombre_archivo)
