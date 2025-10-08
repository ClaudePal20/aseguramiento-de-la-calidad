from logger_config import setup_logger
import requests
import time

# Configurar logger
logger = setup_logger("test_tiempo_prolongado")

URL = "http://localhost:5000/books"
DURATION_SECONDS = 3600  # 1 hora

def test_tiempo_prolongado():
    """Prueba de tiempo prolongado: envía solicitudes repetidas durante 1 hora."""
    logger.info(f"Iniciando prueba de tiempo prolongado ({DURATION_SECONDS} segundos)")

    start = time.time()
    end = start + DURATION_SECONDS
    count = 0

    while time.time() < end:
        try:
            r = requests.get(URL)
            status = r.status_code
            logger.info(f"Iteración {count+1} | Status: {status}")
        except Exception as e:
            logger.error(f"Iteración {count+1} | Error: {e}")
        count += 1
        time.sleep(0.5)  # medio segundo entre peticiones

    logger.info(f"Prueba completada. Total de peticiones: {count}")
    print(f"Total de peticiones en {DURATION_SECONDS} segundos: {count}")

if __name__ == "__main__":
    test_tiempo_prolongado()
