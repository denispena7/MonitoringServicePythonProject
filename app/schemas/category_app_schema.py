from pydantic import BaseModel

class CategoryWithTime(BaseModel):
    categoria: str
    tiempo_empleado: int

    class Config:
        orm_mode = True