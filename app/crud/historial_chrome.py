import sqlite3, os
from app.utils.logger_setup import get_logger
logger = get_logger('MonitorApp')

def conectar_historial_chrome():
    # Ruta al historial de Chrome universal
    history_path = os.path.join(
        os.environ["LOCALAPPDATA"],
        r"Google\Chrome\User Data\Default\History"
    )

    try:
        connection = sqlite3.connect(history_path)
    except sqlite3.OperationalError as e:
        logger.exception(f"Error al conectar a la base de datos: {e}")
        return None
    
    return connection

def obtener_historial(conexion, apertura_chrome, cierre_chrome):
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT url, title, visit_count, last_visit_time 
        FROM urls 
        WHERE last_visit_time BETWEEN ? AND ? 
        ORDER BY last_visit_time DESC
        """, (apertura_chrome, cierre_chrome))
    urls = cursor.fetchall()
    cursor.close()
    return urls