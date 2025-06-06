from __future__ import annotations
from typing import TYPE_CHECKING
from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text

if TYPE_CHECKING:
    from app.models.categoria import Categoria
    from app.models.sesion_app import SesionApp


class Aplicacion(Base):
    __tablename__ = "aplicaciones"

    idAplicacion: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    nombreAplicacion: Mapped[str] = mapped_column(Text, nullable = False)
    esNavegador: Mapped[bool] = mapped_column(nullable = False)
    idCategoriaAppFK: Mapped[int] = mapped_column(ForeignKey("categorias.idCategoria"))

    # Relación bidireccional con categorias
    categoria_app: Mapped["Categoria"] = relationship(back_populates="aplicaciones")

    # Relación bidireccional con sesiones_app
    sesiones_app: Mapped[list["SesionApp"]] = relationship(back_populates="aplicacion")

    def __repr__ (self) -> str:
        return f"Aplicacion(idAplicacion={self.idAplicacion!r}, nombreAplicacion={self.nombreAplicacion!r}, esNavegador={self.esNavegador!r})"