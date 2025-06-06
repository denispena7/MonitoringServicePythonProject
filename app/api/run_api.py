# run_api.py
import sys, os

# Asegura que el directorio 'backend' esté en sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

import uvicorn
from app.api.endpoints import app

def redirigir_logs_api():
    LOG_DIR = os.path.join(os.environ.get('ProgramData', 'C:\\ProgramData'), 'RegistroActividad')
    os.makedirs(LOG_DIR, exist_ok=True)
    api_log_path = os.path.join(LOG_DIR, 'api_log.txt')

    sys.stdout = open(api_log_path, 'a', encoding='utf-8')
    sys.stderr = sys.stdout

def run_api():
     redirigir_logs_api()
     uvicorn.run(app, host="127.0.0.1", port=8000, reload=False, access_log=True)

if __name__ == "__main__":
    run_api()
