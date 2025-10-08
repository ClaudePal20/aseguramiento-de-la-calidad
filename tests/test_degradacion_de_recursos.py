from logger_config import setup_logger
import psutil
import time
import requests

# Configurar logger
logger = setup_logger("test_degradacion_recursos")

URL = "http://localhost:5000/books"

def test_degradacion_recursos():
    """Prueba de degradación de recursos: mide CPU y memoria durante carga sostenida."""
    logger.info("Iniciando prueba de degradación de recursos")

    for i in range(100):
        try:
            r = requests.get(URL)
            status = r.status_code
        except Exception as e:
            status = None
            logger.error(f"Error en la solicitud: {e}")

        cpu = psutil.cpu_percent(interval=0.5)
        mem = psutil.virtual_memory().percent

        msg = f"Iteración {i+1} | Status: {status} | CPU: {cpu}% | Memoria: {mem}%"
        print(msg)
        logger.info(msg)

        time.sleep(1)

    logger.info("Prueba de degradación de recursos completada.\n")

if __name__ == "__main__":
    test_degradacion_recursos()
