from app.utils.json_loader import cargar_categorias_apps, cargar_categorias_web, cargar_nombre_aplicacion

categorias_apps = cargar_categorias_apps()
categorias_web = cargar_categorias_web()
nombres_dict = cargar_nombre_aplicacion()

def clasificar_aplicacion(aplicacion):
    for categoria in categorias_apps:
        for app in categorias_apps[categoria]:
            if app.lower() in aplicacion.lower():
                return categoria
    return "Otros"

def clasificar_web(sitio_web):
    for categoria in categorias_web:
        for web in categorias_web[categoria]:
            if web.lower() in sitio_web.lower():
                return categoria
    return "Otros"

def obtener_nombre_aplicacion(aplicacion):
    for nombre in nombres_dict:
        if aplicacion == nombre:
            return nombres_dict[nombre]
            
    return aplicacion