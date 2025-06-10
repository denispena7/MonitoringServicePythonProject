from threading import Event

from app.utils.utils_register.utils_ventanas import obtener_ventanas_visibles
from app.register.procesador import procesar_ventanas
from app.utils.logger_setup import get_logger

logger = get_logger('MonitorApp')

def registrar_aplicaciones(stop_event: Event):
    ventanas_activas = {}
    logger.info("Monitoreando uso de ventanas. Presiona Ctrl+C para salir.\n")

    ventanas_existentes = set(obtener_ventanas_visibles().keys())
    logger.info("Actualizando ventanas activas...")

    while not stop_event.is_set():
        try:
            ventanas_activas = procesar_ventanas(ventanas_activas, ventanas_existentes)
        except Exception as e:
            logger.exception(f"Error en el hilo de registrar_aplicaciones: {e}")
        stop_event.wait(2)