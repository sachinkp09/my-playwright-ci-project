import logging
from pathlib import Path

# ROOT_DIR points to your project root
ROOT_DIR = Path(__file__).resolve().parent.parent

def get_logger():
    logger = logging.getLogger("playwright-tests")
    logger.setLevel(logging.INFO)

    # Console output (shows logs in terminal + CI)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # File output (ensures logs are saved for CI artifacts)
    log_dir = ROOT_DIR / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)   # Create logs folder if missing
    file_handler = logging.FileHandler(log_dir / "test_log.txt")
    file_handler.setLevel(logging.INFO)

    # Log formatting
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Attach handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
