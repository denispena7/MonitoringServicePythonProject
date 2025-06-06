from app.database.base import Base
from app.database.session import engine

from app.crud.categories import inicializar_categorias
from app.utils import *

from app.models.categoria import Categoria
from app.models.aplicacion import Aplicacion
from app.models.sitio import Sitio
from app.models.sesion_app import SesionApp
from app.models.sesion_web import SesionWeb


from app.utils.logger_setup import get_logger
logger = get_logger('MonitorApp')

def init_db():
    Base.metadata.create_all(bind=engine)
    logger.info("Base de datos inicializada correctamente")

    categorias_apps = cargar_categorias_apps().keys()
    categorias_web = cargar_categorias_web().keys()

    categorias = set(categorias_apps).union(set(categorias_web))

    inicializar_categorias(categorias)

    logger.info("Categorías inicializadas correctamente")