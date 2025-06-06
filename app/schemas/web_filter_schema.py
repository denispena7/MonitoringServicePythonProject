from pydantic import BaseModel

class WebFiltro(BaseModel):
    sitio_web: str
    titulo_sitio_web: str
    numero_visitas: int

    class Config:
        orm_mode = True