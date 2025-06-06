from pydantic import BaseModel

class CategoryWithVisitNumber(BaseModel):
    categoria: str
    numero_visitas: int

    class Config:
        orm_mode = True