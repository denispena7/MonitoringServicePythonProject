import threading, time
from app.register.registro_app import registrar_aplicaciones
from app.register.registro_web_session import monitorear_sesiones_navegador

stop_event_global = threading.Event()

def iniciar_monitoreo_servicio():
    hilo_app = threading.Thread(
        target=registrar_aplicaciones,
        args=(stop_event_global,),
        name="Hilo Monitor Aplicaciones",
        daemon=True
    )

    hilo_web = threading.Thread(
        target=monitorear_sesiones_navegador,
        args=(stop_event_global,),
        name="Hilo Web por Sesión",
        daemon=True
    )

    hilo_app.start()
    hilo_web.start()

    while not stop_event_global.is_set():
        time.sleep(2)

    # Esperar fin de hilos
    hilo_app.join(timeout=2)
    hilo_web.join(timeout=2)

def detener_monitoreo():
    stop_event_global.set()