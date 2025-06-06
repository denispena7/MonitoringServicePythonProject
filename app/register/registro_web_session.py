import threading, psutil
from datetime import datetime
from threading import Event

from app.utils.time_utils import convertir_a_chrome_time, formatear_hora
from app.register.registro_web import registrar_sitios_web

from app.utils.logger_setup import get_logger
logger = get_logger('MonitorApp')

# Configuración de procesos a monitorear
NAVEGADORES = {"chrome.exe", "msedge.exe", "firefox.exe", "opera.exe"}

def navegador_activo(nombre_proceso: str) -> bool:
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and proc.info['name'].lower() == nombre_proceso:
            return True
    return False

def monitorear_sesiones_navegador(stop_event: Event):
    logger.info("🧭 Monitoreando sesiones completas del navegador...")

    procesos_previos = {nav: False for nav in NAVEGADORES}
    tiempos_inicio = {}
    logger.info("🔄 Verificando estado de los navegadores...")

    while not stop_event.is_set():
        try:
            for nav in NAVEGADORES:
                activo = navegador_activo(nav)

                if activo and not procesos_previos[nav]:
                    tiempos_inicio[nav] = datetime.now()
                    procesos_previos[nav] = True
                    logger.info(f"[NAVEGADOR] {nav} iniciado a las {formatear_hora(tiempos_inicio[nav])}")

                elif not activo and procesos_previos[nav]:
                    hora_inicio = tiempos_inicio.get(nav)
                    hora_fin = datetime.now()

                    if hora_inicio:
                        apertura_chrome = convertir_a_chrome_time(formatear_hora(hora_inicio))
                        cierre_chrome = convertir_a_chrome_time(formatear_hora(hora_fin))
                        logger.info(f"[NAVEGADOR] {nav} cerrado a las {formatear_hora(hora_fin)}")

                        threading.Thread(
                            target=registrar_sitios_web,
                        args=(apertura_chrome, cierre_chrome),
                            name=f"Hilo Historial {nav}"
                        ).start()

                    procesos_previos[nav] = False
                    tiempos_inicio.pop(nav, None)

            stop_event.wait(2)
        except Exception as e:
            logger.exception(f"❌ Error en el monitoreo de navegadores: {e}")
            break