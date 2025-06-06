from pydantic import BaseModel
from typing import Optional

class App(BaseModel):
    idAplicacion: Optional[int] = None
    nombreAplicacion: str
    esNavegador: bool
    idCategoriaAppFK: int

    class Config:
        orm_mode = True
