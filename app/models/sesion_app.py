from __future__ import annotations
from typing import TYPE_CHECKING
from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text

if TYPE_CHECKING:
    from app.models.aplicacion import Aplicacion

class SesionApp(Base):
    __tablename__ = "sesiones_app"

    idSesionApp: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    fechaSesion: Mapped[str] = mapped_column(Text, nullable = False)
    inicioSesion: Mapped[str] = mapped_column(Text, nullable = False)
    finSesion: Mapped[str] = mapped_column(Text, nullable = False)
    duracionSesion: Mapped[int] = mapped_column(nullable = False)
    idAplicacionFK: Mapped[int]  = mapped_column(ForeignKey("aplicaciones.idAplicacion"))

    # Relación bidireccional con Aplicacion
    aplicacion: Mapped["Aplicacion"] = relationship(back_populates = "sesiones_app")

    def __repr__ (self) -> str:
        return f"SesionApp(idSesionApp={self.idSesionApp!r}, fechaSesion={self.fechaSesion!r}, inicioSesion={self.inicioSesion!r}, finSesion={self.finSesion!r}, duracionSesion={self.duracionSesion!r})"