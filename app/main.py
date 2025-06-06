import sys, os

# Asegura que el directorio raíz esté en sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 🔎 Coloca esto aquí para depurar
print("Argumentos recibidos:", sys.argv)

from app.database.init_db import init_db
from app.api.run_api import run_api
from app.register.hilo_monitor import iniciar_monitoreo_servicio

if __name__ == "__main__":
    if len(sys.argv) < 2:   
        print("⚠️ Debes indicar un modo: init_db, run_api o monitor.")
        sys.exit(1)  # Esto bien

    modo = sys.argv[1].lower()

    if modo == "init_db":   
        init_db()
    elif modo == "run_api": 
        run_api()
    elif modo == "monitor":
        iniciar_monitoreo_servicio()
    else:
        print(f"⚠️ Modo '{modo}' no reconocido. Usa: init_db, run_api o monitor.")
        sys.exit(1)  # Esto es importante aquí también
