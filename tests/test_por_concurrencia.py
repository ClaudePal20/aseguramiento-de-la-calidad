from logger_config import setup_logger
import requests
import concurrent.futures
import random
import time

# Configurar logger
logger = setup_logger("test_concurrencia")

URL = "http://localhost:5000/books"

def task(i):
    """Realiza GET o POST aleatoriamente y registra el resultado."""
    try:
        if random.random() < 0.3:
            r = requests.post(URL, json={"title": "Nuevo", "author": "Test"})
            action = "POST"
        else:
            r = requests.get(URL)
            action = "GET"

        status = r.status_code
        logger.info(f"Iteración {i+1} | Acción: {action} | Status: {status}")
        return status

    except Exception as e:
        logger.error(f"Iteración {i+1} | Error: {e}")
        return None

def test_concurrencia():
    """Prueba de concurrencia: mezcla de GET y POST simultáneos."""
    logger.info("Iniciando prueba de concurrencia")

    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        results = list(executor.map(task, range(500)))

    duration = time.time() - start
    success = results.count(200)
    fails = len(results) - success

    logger.info(f"Prueba completada en {duration:.2f}s")
    logger.info(f"Solicitudes exitosas: {success}, fallidas: {fails}")
    print(f"Prueba de concurrencia completada en {duration:.2f}s (OK: {success}, Fails: {fails})\n")

if __name__ == "__main__":
    test_concurrencia()
