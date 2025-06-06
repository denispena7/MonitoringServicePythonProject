from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
    idCategoria: Optional[int] = None
    descripcionCategoria: str

    class Config:
        orm_mode = True