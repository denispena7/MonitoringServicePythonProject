import win32gui, win32process, win32api, psutil, re

ventanas_ignorar_regex = [
    r".* - explorador de archivos",
    r"program manager",
    r"host de ventanas emergentes",
    r"experiencia de entrada de windows",
    r"windows shell experience host",
    r"nvidia geforce overlay",
    r"microsoft text input application",
    r"cortana",
    r"start",
    r"inicio",
    r"action center",
    r"configuración",
    r"msn",
    r"widgets de windows",
    r"ventana de desbordamiento de bandeja del sistema\.",
    r"nueva pestaña - google chrome",
    r"nueva pestaña - perfil 1: microsoft​ edge",
    r"nueva pestaña y 1 página más - perfil 1: microsoft​ edge",
    r"nueva pestaña - firefox",
    r"nueva pestaña - opera",
    r"popuphost"
]

def debe_ignorar_titulo(titulo):
    titulo = titulo.lower()
    return any(re.match(patron, titulo) for patron in ventanas_ignorar_regex)

def obtener_nombre_proceso(hwnd):
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        proceso = psutil.Process(pid)
        return proceso.name().lower(), proceso.exe()
    except Exception:
        return None, None

def obtener_nombre_amigable(exe_path):
    try:
        info = win32api.GetFileVersionInfo(exe_path, '\\')
        trans = info['VarFileInfo']['Translation'][0]
        lang_codepage = f"{trans[0]:04x}{trans[1]:04x}"
        product_name = win32api.GetFileVersionInfo(exe_path, f'\\StringFileInfo\\{lang_codepage}\\ProductName')
        return product_name
    except Exception:
        return None

def obtener_ventanas_visibles():
    visibles = {}

    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            titulo = win32gui.GetWindowText(hwnd).strip()
            if not titulo or debe_ignorar_titulo(titulo):
                return

            proceso, exe_path = obtener_nombre_proceso(hwnd)
            if not proceso:
                return

            # Usamos el ejecutable como clave única
            clave = proceso

            # Mostramos el nombre amigable si existe, o el ejecutable
            mostrar = obtener_nombre_amigable(exe_path) or proceso

            visibles[clave] = (mostrar, proceso)

    win32gui.EnumWindows(callback, None)
    return visibles
