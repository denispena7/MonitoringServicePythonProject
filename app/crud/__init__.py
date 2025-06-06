# app/crud/__init__.py

from .categories import devolver_id_categoria
from .webs import registrar_sitio_web, verficar_sitio, devolver_id_sitio_web, registrar_sesion_web
from .historial_chrome import conectar_historial_chrome, obtener_historial