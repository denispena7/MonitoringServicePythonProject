import os, logging

def get_logger(nombre='MonitorApp', nivel=logging.INFO):
    LOG_DIR = os.path.join(os.environ.get('ProgramData', 'C:\\ProgramData'), 'RegistroActividad')
    os.makedirs(LOG_DIR, exist_ok=True)
    LOG_FILE = os.path.join(LOG_DIR, 'monitoreo.log')

    logger = logging.getLogger(nombre)
    logger.setLevel(nivel)

    # Evita añadir múltiples handlers si ya están configurados
    if not logger.handlers:
        # Handler para archivo
        fh = logging.FileHandler(LOG_FILE, encoding='utf-8')
        fh.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s'))
        logger.addHandler(fh)

        # Handler opcional para consola (útil si corres manualmente)
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s'))
        logger.addHandler(ch)

    return logger
