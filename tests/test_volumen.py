from logger_config import setup_logger
import requests
import time

# Configurar logger
logger = setup_logger("test_volumen")

URL = "http://localhost:5000/books"
TOTAL_LIBROS = 10000
NOTIFY_EVERY = 1000

def test_volumen():
    """Prueba de volumen: inserta 10k libros y mide tiempo de respuesta."""
    logger.info(f"Iniciando prueba de volumen: {TOTAL_LIBROS} libros")

    # Insertar libros
    for i in range(TOTAL_LIBROS):
        data = {"title": f"Libro {i+1}", "author": "Autor X"}
        try:
            r = requests.post(URL, json=data)
            status = r.status_code
            if status != 201 and status != 200:
                logger.warning(f"Libro {i+1} fallo con status {status}")
        except Exception as e:
            logger.error(f"Libro {i+1} error: {e}")
        if (i+1) % NOTIFY_EVERY == 0:
            msg = f"{i+1} libros añadidos"
            print(msg)
            logger.info(msg)

    # Medir tiempo de respuesta para GET con todos los libros
    start = time.time()
    try:
        r = requests.get(URL)
        status = r.status_code
    except Exception as e:
        logger.error(f"Error en GET final: {e}")
        status = None
    duration = time.time() - start

    msg = f"Tiempo de respuesta con {TOTAL_LIBROS} libros: {duration:.2f}s | Status GET: {status}"
    print(msg)
    logger.info(msg)

    logger.info("Prueba de volumen completada.\n")

if __name__ == "__main__":
    test_volumen()
