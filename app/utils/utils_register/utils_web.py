from urllib.parse import urlparse

def obtener_url_raiz(url):
    try:
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}/"
    except Exception:
        return url  # retorna la URL original si no se puede analizar