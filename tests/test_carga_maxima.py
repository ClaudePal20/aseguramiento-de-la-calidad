from logger_config import setup_logger
import time
import requests

logger = setup_logger("test_carga_maxima")

def test_carga_maxima():
    logger.info("Iniciando test de carga máxima")

    url = "http://localhost:5000"
    start_time = time.time()

    try:
        for i in range(1000):
            r = requests.get(url)
            if r.status_code == 200:
                logger.info(f"Petición {i+1} exitosa")
            else:
                logger.warning(f"Petición {i+1} falló con código {r.status_code}")
    except Exception as e:
        logger.error(f"Error durante la test: {e}")

    duration = time.time() - start_time
    logger.info(f"test completada en {duration:.2f} segundos\n")

if __name__ == "__main__":
    test_carga_maxima()
