from __future__ import annotations
from typing import TYPE_CHECKING
from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text, UniqueConstraint

if TYPE_CHECKING:
    from app.models.sitio import Sitio

class SesionWeb(Base):
    __tablename__ = "sesiones_web"

    idSesionWeb: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    fechaSesion: Mapped[str] = mapped_column(Text, nullable = False)
    horaSesion: Mapped[str] = mapped_column(Text, nullable = False)
    numeroVisitas: Mapped[int] = mapped_column(nullable = False)
    idSitioWebFK: Mapped[int] = mapped_column(ForeignKey("sitios_web.idSitioWeb"))

    sitio_web: Mapped["Sitio"] = relationship(back_populates = "sesiones_web")

    __table_args__ = (
        UniqueConstraint('fechaSesion', 'horaSesion', 'idSitioWebFK', name='idx_sesion_web_unica'),
    )

    def __repr__ (self) -> str:
        return f"SesionWeb(idSesionWeb={self.idSesionWeb!r}, fechaSesion={self.fechaSesion!r}, horaSesion={self.horaSesion!r}, numeroVisitas={self.numeroVisitas!r})"
