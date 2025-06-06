from app.models.categoria import Categoria

from app.database.session import SessionLocal

from app.utils.logger_setup import get_logger
logger = get_logger('MonitorApp')

def devolver_id_categoria(categoria: str) -> int:
    session = SessionLocal()
    try:
        categoria_obj = session.query(Categoria).filter(Categoria.descripcionCategoria == categoria).first()
        if categoria_obj:
            return categoria_obj.idCategoria
        else:
            logger.info(f"No se encontró la categoría '{categoria}' en la base de datos.")
            return -1
    except Exception as e:
        logger.exception(f"Error al obtener el ID de la categoría '{categoria}': {e}")
        raise
    finally:
        session.close()

def create_categoria(categoria: Categoria):
    session = SessionLocal()
    try:
        session.add(categoria)
        session.commit()  # commit hace flush automáticamente
        logger.info(f"Categoría añadida con ID: {categoria.idCategoria}")
    except Exception as e:
        logger.exception(f"Error al registrar la categoría: {e}")
        session.rollback()
        raise
    finally:
        session.close()

def inicializar_categorias(nombres: list[str]):
    session = SessionLocal()
    try:
        categorias = [Categoria(descripcionCategoria=nombre) for nombre in nombres]
        session.add_all(categorias)
        session.commit()
        logger.info(f"Categorías inicializadas: {[categoria.descripcionCategoria for categoria in categorias]}")
    except Exception as e:
        logger.exception(f"Error al inicializar las categorías: {e}")
        session.rollback()
        raise
    finally:
        session.close()