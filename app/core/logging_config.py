import logging
from logging.config import dictConfig
from logging.handlers import RotatingFileHandler

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
        },
        "file": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/app.log",
            "maxBytes": 10 * 1024 * 1024,  # max 10 MB each
            "backupCount": 5,  # keep 5 files
        },
    },
    "loggers": {
        "": {"handlers": ["console", "file"], "level": "INFO", "propagate": True},
    },
}

# Apply logging configuration
dictConfig(LOGGING_CONFIG)
