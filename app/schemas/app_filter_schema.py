from pydantic import BaseModel

class AppFiltro(BaseModel):
    id_app: int
    aplicacion: str
    tiempo_empleado: int

    class Config:
        orm_mode = True