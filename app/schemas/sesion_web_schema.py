from pydantic import BaseModel
from typing import Optional

class Sesion_Web(BaseModel):
    idSesionWeb: Optional[int] = None
    fechaSesion: str
    horaSesion: str
    numeroVisitas: int
    idSitioWebFK: int

    class Config:
        orm_mode = True