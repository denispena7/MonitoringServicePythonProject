from app.database.session import SessionLocal

from app.models.aplicacion import Aplicacion
from app.models.sesion_app import SesionApp

from app.utils.logger_setup import get_logger
logger = get_logger('MonitorApp')

def verficar_aplicacion(nombre: str) -> bool:
    session = SessionLocal()
    try:
        aplicacion_obj = session.query(Aplicacion).filter(Aplicacion.nombreAplicacion == nombre).first()
        if aplicacion_obj:
            logger.info(f"La aplicación '{nombre}' ya existe en la base de datos.")
            return True
        else:
            logger.info(f"La aplicación '{nombre}' no existe en la base de datos.")
            return False
    except Exception as e:
        logger.exception(f"Error al verificar la aplicación '{nombre}': {e}")
        raise
    finally:
        session.close()

def devolver_id_aplicacion(nombre: str) -> int:
    session = SessionLocal()
    try:
        aplicacion_obj = session.query(Aplicacion).filter(Aplicacion.nombreAplicacion == nombre).first()
        if aplicacion_obj:
            return aplicacion_obj.idAplicacion
        else:
            logger.info(f"No se encontró la aplicación '{nombre}' en la base de datos.")
            return -1
    except Exception as e:
        logger.exception(f"Error al obtener el ID de la aplicación '{nombre}': {e}")
        raise
    finally:
        session.close()

def registrar_app(app: Aplicacion):
    session = SessionLocal()
    try:
        session.add(app)
        session.commit()  # commit hace flush automáticamente
        logger.info(f"Aplicación añadida con ID: {app.idAplicacion}")
    except Exception as e:
        logger.exception(f"Error al registrar la aplicación: {e}")
        session.rollback()
        raise
    finally:
        session.close()

def registrar_sesion_app(sesion_app: SesionApp):
    session = SessionLocal()
    try:
        session.add(sesion_app)
        session.commit()  # commit hace flush automáticamente
        logger.info(f"Sesión de aplicación añadida con ID: {sesion_app.idSesionApp}")
    except Exception as e:
        logger.exception(f"Error al registrar la sesión de aplicación: {e}")
        session.rollback()
        raise
    finally:
        session.close()
