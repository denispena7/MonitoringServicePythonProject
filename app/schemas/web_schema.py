from pydantic import BaseModel
from typing import Optional

class Web(BaseModel):
    idSitioWeb: Optional[int] = None
    urlSitioWeb: str
    tituloSitioWeb: str
    idCategoriaWebFK: int

    class Config:
        orm_mode = True