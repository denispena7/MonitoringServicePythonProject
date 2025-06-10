from pydantic import BaseModel

class WebFiltro(BaseModel):
    id_sitioweb: int
    sitio_web: str
    titulo_sitio_web: str
    numero_visitas: int
    categoria: str
    id_cat: int

    class Config:
        orm_mode = True