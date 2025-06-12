from pydantic import BaseModel

class CategoryWithVisitNumber(BaseModel):
    id: int
    categoria: str
    numero_visitas: int

    class Config:
        orm_mode = True