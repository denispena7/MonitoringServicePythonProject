from app.models import *
from app.crud import *
from app.utils import *

from app.utils.logger_setup import get_logger
logger = get_logger('MonitorApp')

def registrar_sitios_web(hora_inicio_sesion, hora_fin_sesion):
    con = conectar_historial_chrome()
    logger.info(f"[HILO WEB] Lanzado con intervalo {hora_inicio_sesion} → {hora_fin_sesion}")

    try:
        if hora_inicio_sesion < hora_fin_sesion:

            urls = obtener_historial(con, hora_inicio_sesion, hora_fin_sesion)
            logger.info("Conexión a la base de datos establecida.")

            for url, title, visit_count, last_visit_time in urls:
                formatted_date = time_utils.chrome_time_to_datetime(last_visit_time)
                visit_date = formateo_mysql_fechas(formatted_date)
                visit_time = formatear_hora(formatted_date)
                raiz = obtener_url_raiz(url)
                categoria = clasificar_web(raiz) if raiz else "Otros"

                cat = devolver_id_categoria(categoria)

                sitio = Sitio(
                    urlSitioWeb = raiz,
                    tituloSitioWeb = title,
                    idCategoriaWebFK = cat
                )

                if not verficar_sitio(sitio.urlSitioWeb):
                    registrar_sitio_web(sitio)

                id_web = devolver_id_sitio_web(sitio.urlSitioWeb)

                sesion_web = SesionWeb(
                    fechaSesion = visit_date,
                    horaSesion = visit_time,
                    numeroVisitas = visit_count,
                    idSitioWebFK = id_web
                )

                registrar_sesion_web(sesion_web)

                logger.info(f"Título: {title} | URL: {raiz} | Visitas: {visit_count} | Fecha: {visit_date} | Hora: {visit_time} | Categoría: {categoria}")
        else:
            logger.error("Error: La hora de inicio de sesión debe ser menor que la hora de cierre de sesión.")
    except Exception as e:
        logger.exception(f"Error al registrar sitios web: {e}")