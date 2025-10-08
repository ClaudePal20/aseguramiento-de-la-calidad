from logger_config import setup_logger
import requests
import concurrent.futures
import time

# Configurar logger
logger = setup_logger("test_spike")

URL = "http://localhost:5000/books"

def get_books(_):
    """Realiza una petición GET y devuelve el código de estado."""
    try:
        response = requests.get(URL)
        return response.status_code
    except Exception as e:
        logger.error(f"Error en la solicitud: {e}")
        return None

def test_spike():
    """Prueba de picos (spike test): simula aumentos súbitos de usuarios."""
    logger.info("Iniciando prueba de picos (Spike Test)")

    for users in [10, 50, 200, 500]:
        start = time.time()

        with concurrent.futures.ThreadPoolExecutor(max_workers=users) as executor:
            results = list(executor.map(get_books, range(users)))

        duration = time.time() - start
        success = results.count(200)
        fails = len(results) - success

        logger.info(f"Spike a {users} usuarios completado en {duration:.2f}s")
        logger.info(f"Solicitudes exitosas: {success}, fallidas: {fails}")

        print(f"Spike a {users} usuarios: {duration:.2f}s (OK: {success}, Fails: {fails})")

    logger.info("Prueba de picos completada.\n")

if __name__ == "__main__":
    test_spike()
