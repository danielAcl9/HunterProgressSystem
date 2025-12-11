"""Logging configuration for the API module."""

import logging
import sys
from pathlib import Path

def setup_logging():
    """Set up logging configuration for the API module."""

    # Create logs folder if not exists
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok = True)

    # Setup format
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    # Setup genertal logging
    logging.basicConfig(
        level = logging.INFO,
        format = log_format,
        datefmt = date_format,
        handlers = [
            # Console handler
            logging.StreamHandler(sys.stdout),
            # File handler para todos los logs
            logging.FileHandler("logs/app.log"),
            # File handler solo para errores
            logging.FileHandler("logs/error.log")
        ]
    )

    # Setup uvicorn logger
    logging.getLogger("uvicorn.access").handlers = []
    logging.getLogger("uvicorn.error").handlers = []

    return logging.getLogger("hunter_api")

# Global logger

logger = setup_logging()