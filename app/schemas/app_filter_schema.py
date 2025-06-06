from pydantic import BaseModel

class AppFiltro(BaseModel):
    aplicacion: str
    tiempo_empleado: int

    class Config:
        orm_mode = True