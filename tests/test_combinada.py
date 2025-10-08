from logger_config import setup_logger
import requests
import concurrent.futures
import random
import time

# Configurar logger
logger = setup_logger("test_combinada")

URL = "http://localhost:5000/books"

def mixed_task(i):
    """Realiza POST, GET o búsqueda aleatoria y registra el resultado."""
    try:
        r_value = random.random()
        if r_value < 0.1:
            r = requests.post(URL, json={"title": "Libro Random", "author": "Mix"})
            action = "POST"
        elif r_value < 0.8:
            r = requests.get(URL)
            action = "GET"
        else:
            r = requests.get(URL + "/search?q=libro")
            action = "SEARCH"

        status = r.status_code
        logger.info(f"Iteración {i+1} | Acción: {action} | Status: {status}")
        return status

    except Exception as e:
        logger.error(f"Iteración {i+1} | Error: {e}")
        return None

def test_combinada():
    """Prueba combinada: mezcla de operaciones con concurrencia incremental."""
    logger.info("Iniciando prueba combinada")

    for step in range(5):
        users = (step + 1) * 50
        start = time.time()

        with concurrent.futures.ThreadPoolExecutor(max_workers=users) as executor:
            results = list(executor.map(mixed_task, range(500)))

        duration = time.time() - start
        success = results.count(200)
        fails = len(results) - success

        msg = f"Etapa {step+1} - Usuarios: {users} | Tiempo: {duration:.2f}s | OK: {success}, Fails: {fails}"
        print(msg)
        logger.info(msg)

    logger.info("Prueba combinada completada.\n")

if __name__ == "__main__":
    test_combinada()
