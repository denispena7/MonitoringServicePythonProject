import datetime
from zoneinfo import ZoneInfo

# Funciones para formatear fechas y horas
def formateo_europeo_fechas(dt):
    return dt.strftime("%d/%m/%Y")

def formateo_mysql_fechas(dt):
    return dt.strftime("%Y-%m-%d")

def formatear_hora(dt):
    return dt.strftime("%H:%M:%S")

# Función para convertir el tiempo de Chrome a un objeto datetime
def chrome_time_to_datetime(chrome_time):
    epoch_start = datetime.datetime(1601, 1, 1, tzinfo=datetime.timezone.utc)
    delta = datetime.timedelta(microseconds=chrome_time)
    utc_time = epoch_start + delta
    return utc_time.astimezone(ZoneInfo("Europe/Madrid"))

def convertir_a_chrome_time(time_str: str, date_base: datetime.date = None, tz: str = "Europe/Madrid") -> int:
    # Usa la fecha de hoy si no se proporciona una base
    if date_base is None:
        date_base = datetime.date.today()

    # Combina la fecha base con la hora proporcionada
    local_dt = datetime.datetime.strptime(f"{date_base} {time_str}", "%Y-%m-%d %H:%M:%S")
    local_dt = local_dt.replace(tzinfo=ZoneInfo(tz))

    # Convierte a UTC
    dt_utc = local_dt.astimezone(datetime.timezone.utc)

    # Epoch de Chrome
    epoch_start = datetime.datetime(1601, 1, 1, tzinfo=datetime.timezone.utc)
    delta = dt_utc - epoch_start
    return int(delta.total_seconds() * 1_000_000)  # microsegundos


# Obtener la fecha y hora actual
def fecha_hoy():
    return datetime.datetime.now(ZoneInfo("Europe/Madrid")).strftime("%Y-%m-%d")

# Obtener los segundos transcurridos entre dos horas
def calcular_duracion_en_segundos(inicio, fin):
    return int((fin - inicio).total_seconds())
