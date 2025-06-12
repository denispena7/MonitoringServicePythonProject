from pydantic import BaseModel

class CategoryWithTime(BaseModel):
    id: int
    categoria: str
    tiempo_empleado: int

    class Config:
        orm_mode = True