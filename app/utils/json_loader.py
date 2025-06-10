import json
import os
import sys

from app.utils.logger_setup import get_logger
logger = get_logger('MonitorApp')

def obtener_ruta_absoluta(relativa):
    """
    Devuelve la ruta absoluta al archivo de datos empaquetado (o en desarrollo).
    """
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    return os.path.join(base_path, relativa)

def cargar_json(nombre_archivo):
    # Usa la nueva forma de obtener la ruta absoluta
    ruta = obtener_ruta_absoluta(os.path.join('config', nombre_archivo))
    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.exception(f"No se encontró el archivo {nombre_archivo} en: {ruta}")
    except json.JSONDecodeError:
        logger.exception(f"Error al decodificar el archivo {nombre_archivo}. Revisa el formato.")
    return {}

def cargar_categorias_apps():
    return cargar_json('categorias_aplicaciones.json')

def cargar_categorias_web():
    return cargar_json('categorias_sitios_web.json')

def cargar_nombre_aplicacion():
    return cargar_json('nombre_ejecutables.json')
