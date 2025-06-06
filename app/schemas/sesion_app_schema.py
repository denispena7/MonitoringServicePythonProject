from pydantic import BaseModel
from typing import Optional

class Sesion_App(BaseModel):
    idSesionApp: Optional[int] = None
    fechaSesion: str
    inicioSesion: str
    finSesion: str
    duracionSesion: int
    idAplicacionFK: int

    class Config:
        orm_mode = True