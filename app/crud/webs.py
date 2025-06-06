from app.models.sitio import Sitio
from app.models.sesion_web import SesionWeb

from app.database.session import SessionLocal

from app.utils.logger_setup import get_logger
logger = get_logger('MonitorApp')

def verficar_sitio(url: str) -> bool:
    session = SessionLocal()
    try:
        sitio_obj = session.query(Sitio).filter(Sitio.urlSitioWeb == url).first()
        if sitio_obj:
            logger.info(f"El sitio '{url}' ya existe en la base de datos.")
            return True
        else:
            logger.info(f"El sitio '{url}' no existe en la base de datos.")
            return False
    except Exception as e:
        logger.exception(f"Error al verificar el sitio '{url}': {e}")
        raise
    finally:
        session.close()

def devolver_id_sitio_web(url: str) -> int:
    session = SessionLocal()
    try:
        sitio_obj = session.query(Sitio).filter(Sitio.urlSitioWeb == url).first()
        if sitio_obj:
            return sitio_obj.idSitioWeb
        else:
            logger.info(f"No se encontró la aplicación '{url}' en la base de datos.")
            return -1
    except Exception as e:
        logger.exception(f"Error al obtener el ID del sitio '{url}': {e}")
        raise
    finally:
        session.close()

def registrar_sitio_web(web: Sitio):
    session = SessionLocal()
    try:
        session.add(web)
        session.commit()  # commit hace flush automáticamente
        logger.info(f"Sitio web añadido con ID: {web.idSitioWeb}")
    except Exception as e:
        logger.exception(f"Error al registrar el sitio web: {e}")
        session.rollback()
        raise
    finally:
        session.close()

def registrar_sesion_web(sesion_web: SesionWeb):
    session = SessionLocal()
    try:
        session.add(sesion_web)
        session.commit()  # commit hace flush automáticamente
        logger.info(f"Sesión de sitio web añadida con ID: {sesion_web.idSesionWeb}")
    except Exception as e:
        logger.exception(f"Error al registrar la sesión de sitio web: {e}")
        session.rollback()
        raise
    finally:
        session.close()