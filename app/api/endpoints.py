from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends, Query

from sqlalchemy import select, func, and_
from sqlalchemy.orm import Session

from app.database.session import SessionLocal

import traceback

from app.schemas import *
from app.models import *

app = FastAPI()

# Dependencia
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Consulta para sacar categorias
@app.get("/categorias", response_model = List[Category])
def get_categories(db: Session = Depends(get_db)):
    stmt = (
        select(Categoria)
        .order_by(Categoria.descripcionCategoria)
    )
    result = db.execute(stmt).all()
    return db.execute(stmt).scalars().all()

# Consulta para sacar top 10 de apps por su tiempo de uso
@app.get("/apps", response_model=List[App])
def get_top_apps(db: Session = Depends(get_db)):
    stmt = (
        select(Aplicacion)
        .join(SesionApp, Aplicacion.idAplicacion == SesionApp.idAplicacionFK)
        .group_by(Aplicacion.nombreAplicacion)
        .order_by(func.sum(SesionApp.duracionSesion).desc())
        .limit(10)
    )
    return db.execute(stmt).scalars().all()

# Consulta para sacar top 10 de categorias de aplicaciones por su tiempo de uso
@app.get('/categorias_apps', response_model=List[CategoryWithTime])
def get_top_appcats(db: Session = Depends(get_db)):
    stmt = (
        select(
            Categoria.descripcionCategoria.label("categoria"),
            func.sum(SesionApp.duracionSesion).label("tiempo_empleado")
        )
        .join(Aplicacion, Categoria.idCategoria == Aplicacion.idCategoriaAppFK)
        .join(SesionApp, Aplicacion.idAplicacion == SesionApp.idAplicacionFK)
        .group_by(Categoria.descripcionCategoria)
        .order_by(func.sum(SesionApp.duracionSesion).desc())
        .limit(10)
    )

    result = db.execute(stmt).all()
    return [
        {"categoria": row._mapping["categoria"], "tiempo_empleado": row._mapping["tiempo_empleado"]}
        for row in result
    ]

# Consulta para sacar aplicaciones según filtros de categorias y uso
@app.get('/filtros_app', response_model=List[AppFiltro])
def get_filtered_apps(
    categoria_id: Optional[int] = Query(None),
    fecha_inicio: str = Query(...),
    fecha_fin: str = Query(...),
    db: Session = Depends(get_db)
):
    try:
        condiciones = [
            SesionApp.fechaSesion.between(fecha_inicio, fecha_fin)
        ]
        
        if categoria_id is not None:
            condiciones.append(Aplicacion.idCategoriaAppFK == categoria_id)

        stmt = (
            select(
                Aplicacion.nombreAplicacion.label("aplicacion"),
                func.sum(SesionApp.duracionSesion).label("tiempo_empleado")
            )
            .join(SesionApp, Aplicacion.idAplicacion == SesionApp.idAplicacionFK)
            .where(and_(*condiciones))
            .group_by(Aplicacion.nombreAplicacion)
            .order_by(func.sum(SesionApp.duracionSesion).desc())
        )

        result = db.execute(stmt).all()

        return [
            {"aplicacion": row._mapping["aplicacion"], "tiempo_empleado": row._mapping["tiempo_empleado"]}
            for row in result
        ]
    except Exception as e:
        traceback.print_exc() 
        raise HTTPException(status_code=500, detail=str(e))
    
# Consulta para sacar top 10 de sitios web por su número de visitas
@app.get('/sitios_web', response_model = List[Web])
def get_top_webs(db: Session = Depends(get_db)):
    stmt = (
        select(Sitio)
        .join(SesionWeb, Sitio.idSitioWeb == SesionWeb.idSitioWebFK)
        .group_by(Sitio.urlSitioWeb)
        .order_by(func.sum(SesionWeb.numeroVisitas).desc())
        .limit(10)
    )
    return db.execute(stmt).scalars().all()


# Consulta para sacar top 10 de categorias de sitios web por el número de visitas
@app.get('/categorias_web', response_model=List[CategoryWithVisitNumber])
def get_top_webcats(db: Session = Depends(get_db)):
    stmt = (
        select(
            Categoria.descripcionCategoria.label("categoria"),
            func.sum(SesionWeb.numeroVisitas).label("numero_visitas")
        )
        .join(Sitio, Categoria.idCategoria == Sitio.idCategoriaWebFK)
        .join(SesionWeb, Sitio.idSitioWeb == SesionWeb.idSitioWebFK)
        .group_by(Categoria.descripcionCategoria)
        .order_by(func.sum(SesionWeb.numeroVisitas).desc())
        .limit(10)
    )

    result = db.execute(stmt).all()
    return [
        {"categoria": row._mapping["categoria"], "numero_visitas": row._mapping["numero_visitas"]}
        for row in result
    ]

# Consulta para sacar sitios web según filtros de categorias y uso
@app.get('/filtros_web', response_model=List[WebFiltro])
def get_filtered_websites(
    categoria_id: Optional[int] = Query(None),
    fecha_inicio: str = Query(...),
    fecha_fin: str = Query(...),
    db: Session = Depends(get_db)
):
    try:
        condiciones = [
            SesionWeb.fechaSesion.between(fecha_inicio, fecha_fin)
        ]
        
        if categoria_id is not None:
            condiciones.append(Sitio.idCategoriaWebFK == categoria_id)

        stmt = (
            select(
                Sitio.urlSitioWeb.label("sitio_web"),
                Sitio.tituloSitioWeb.label("titulo_sitio_web"),
                func.sum(SesionWeb.numeroVisitas).label("numero_visitas")
            )
            .join(SesionWeb, Sitio.idSitioWeb == SesionWeb.idSitioWebFK)
            .where(and_(*condiciones))
            .group_by(Sitio.urlSitioWeb)
            .order_by(func.sum(SesionWeb.numeroVisitas).desc())
        )

        result = db.execute(stmt).all()

        return [
            {"sitio_web": row._mapping["sitio_web"], "titulo_sitio_web": row._mapping["titulo_sitio_web"], "numero_visitas": row._mapping["numero_visitas"]}
            for row in result
        ]
    except Exception as e:
        traceback.print_exc() 
        raise HTTPException(status_code=500, detail=str(e))