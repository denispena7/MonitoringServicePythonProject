from __future__ import annotations
from typing import TYPE_CHECKING
from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text

if TYPE_CHECKING:
    from app.models.categoria import Categoria
    from app.models.sesion_web import SesionWeb

class Sitio(Base):
    __tablename__ = "sitios_web"

    idSitioWeb: Mapped[int] = mapped_column(primary_key = True, autoincrement = True) 
    urlSitioWeb: Mapped[str] = mapped_column(Text, nullable = False)
    tituloSitioWeb: Mapped[str] = mapped_column(Text, nullable = False)
    idCategoriaWebFK: Mapped[int] = mapped_column(ForeignKey("categorias.idCategoria"))

    # Relación bidireccional
    categoria_sitio: Mapped["Categoria"] = relationship(back_populates = "sitios_web")

    # Relación bidireccional con sesiones_web
    sesiones_web: Mapped[list["SesionWeb"]] = relationship(back_populates="sitio_web")

    def __repr__ (self) -> str:
        return f"Sitio(idSitioWeb={self.idSitioWeb!r}, urlSitioWeb={self.urlSitioWeb!r}, tituloSitioWeb={self.tituloSitioWeb!r})"