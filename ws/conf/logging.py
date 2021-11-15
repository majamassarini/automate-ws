import logging  # noqa
import os


def default_logging_configuration(logging_dir, logging_level="INFO"):
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s - %(name)s:%(lineno)d %(levelname)s - %(message)s",
            },
            "collector": {
                "format": "%(asctime)s - %(message)s",
            },
        },
        "handlers": {
            "console": {
                "formatter": "simple",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "webserver": {
                "formatter": "simple",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": os.path.join(logging_dir, "webserver.log"),
                "when": "midnight",
                "interval": 1,
            },
            "home": {
                "formatter": "simple",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": os.path.join(logging_dir, "webserver-home.log"),
                "when": "midnight",
                "interval": 1,
            },
        },
        "loggers": {
            "": {
                "level": "WARNING",
                "handlers": ["console", "webserver"],
                "propagate": True,
            },
            "asyncio": {
                "level": "WARNING",
                "handlers": ["console", "webserver"],
                "propagate": False,
            },
            "apscheduler": {
                "level": "WARNING",
                "handlers": ["console", "webserver"],
                "propagate": False,
            },
            "aiohttp": {
                "level": "DEBUG",
                "handlers": ["console", "webserver"],
                "propagate": False,
            },
            "__main__": {
                "level": logging_level,
                "handlers": ["console", "webserver"],
                "propagate": False,
            },
            "ws": {
                "level": logging_level,
                "handlers": ["console", "webserver"],
                "propagate": False,
            },
            "home": {
                "level": logging_level,
                "handlers": ["console", "home"],
                "propagate": False,
            },
        },
    }
