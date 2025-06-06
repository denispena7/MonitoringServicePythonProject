import datetime
from app.utils.utils_register.clasificador import clasificar_aplicacion, obtener_nombre_aplicacion
from app.utils.utils_register.utils_ventanas import obtener_ventanas_visibles
from app.utils.time_utils import calcular_duracion_en_segundos, formatear_hora, formateo_mysql_fechas
from app.models.aplicacion import Aplicacion
from app.models.sesion_app import SesionApp 
from app.crud.apps import devolver_id_aplicacion, registrar_app, registrar_sesion_app, verficar_aplicacion
from app.crud.categories import devolver_id_categoria
from app.utils.logger_setup import get_logger
logger = get_logger('MonitorApp')

navegadores = {"chrome.exe", "msedge.exe", "firefox.exe", "opera.exe"}

def procesar_ventanas(ventanas_activas, ventanas_existentes):
    # logger.info("🔍 Entrando a procesar_ventanas()")
    nuevas_activas = {}

    ventanas_actuales_dict = obtener_ventanas_visibles()
    # logger.info(f"🔍 Ventanas actuales detectadas: {ventanas_actuales_dict.keys()}")
    ventanas_actuales = set(ventanas_actuales_dict.keys())

    nuevas = ventanas_actuales - ventanas_activas.keys() - ventanas_existentes
    # logger.info(f"🔍 Nuevas ventanas detectadas: {nuevas}")
    for clave in nuevas:
        mostrar, proceso = ventanas_actuales_dict[clave]
        ventanas_activas[clave] = (datetime.datetime.now(), mostrar, proceso)

    cerradas = list(ventanas_activas.keys() - ventanas_actuales)
    # logger.info(f"🔍 Ventanas cerradas detectadas: {cerradas}")
    for clave in cerradas:
        fecha = datetime.datetime.now()
        hora_inicio, nombre, proceso = ventanas_activas.pop(clave)
        hora_fin = datetime.datetime.now()
        duracion = calcular_duracion_en_segundos(hora_inicio, hora_fin)

        if duracion > 8:
            nombre_app = obtener_nombre_aplicacion(nombre)
            fecha_sesion = formateo_mysql_fechas(fecha)
            inicio_sesion = formatear_hora(hora_inicio)
            fin_sesion = formatear_hora(hora_fin)
            es_navegador = proceso in navegadores
            categoria = clasificar_aplicacion(proceso) if proceso else "Otros"

            logger.info(f"🔍 Preparando inserción de sesión: {nombre_app}, Duración: {duracion}s")

            cat = devolver_id_categoria(categoria)

            app = Aplicacion(
                nombreAplicacion = nombre_app,
                esNavegador = es_navegador,
                idCategoriaAppFK = cat
            )

            if not verficar_aplicacion(app.nombreAplicacion):
                logger.info(f"🆕 Registrando nueva aplicación: {app.nombreAplicacion}")
                registrar_app(app)

            id_aplicacion = devolver_id_aplicacion(app.nombreAplicacion)

            sesion_app = SesionApp(
                fechaSesion = fecha_sesion,
                inicioSesion = inicio_sesion,
                finSesion = fin_sesion,
                duracionSesion = duracion,
                idAplicacionFK = id_aplicacion
            )

            registrar_sesion_app(sesion_app)

            logger.info(f'🆕 Título: "{nombre_app}" | '
                f'Fecha: {fecha_sesion} | Inicio: {inicio_sesion} | Fin: {fin_sesion} '
                f'| Duración (s): {int(duracion)}s | Navegador: {es_navegador}  | Categoría: {categoria}')
        else:
                logger.error("Duración demasiado corta, el registro no se guardará.")

    return {**ventanas_activas, **nuevas_activas}