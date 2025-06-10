from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.utils.logger_setup import get_logger
logger = get_logger('MonitorApp')

DATABASE_URL = "sqlite:///C:/ProgramData/RegistroActividad/registro_actividad.db"
logger.info(f"Usando base de datos en: {DATABASE_URL}")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

with engine.connect() as conn:
    conn.execute(text("PRAGMA journal_mode=WAL;"))
    logger.info("Modo WAL activado para SQLite.")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
