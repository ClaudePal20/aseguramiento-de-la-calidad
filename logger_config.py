import logging
import os

def setup_logger(test_name="general"):
    os.makedirs("resultados", exist_ok=True)
    log_path = f"resultados/{test_name}.log"

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logger = logging.getLogger(test_name)
    return logger
