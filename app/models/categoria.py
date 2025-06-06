from __future__ import annotations
from typing import TYPE_CHECKING
from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text

if TYPE_CHECKING:
    from app.models.aplicacion import Aplicacion
    from app.models.sitio import Sitio

class Categoria(Base):
    __tablename__ = "categorias"

    idCategoria: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    descripcionCategoria: Mapped[str] = mapped_column(Text, nullable = False)

    # Relación bidireccional
    aplicaciones: Mapped[list["Aplicacion"]] = relationship(back_populates="categoria_app")
    sitios_web: Mapped[list["Sitio"]] = relationship(back_populates="categoria_sitio")

    def __repr__ (self) -> str:
        return f"Categoria(id={self.idCategoria!r}, descripcionCategoria={self.descripcionCategoria!r})"
    