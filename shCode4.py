import logging
from logging import Logger, Handler, Filter
from logging.config import fileConfig, dictConfig

logging.basicConfig()  # Sensitive

logging.disable()  # Sensitive


def update_logging(logger_class):
    logging.setLoggerClass(logger_class)  # Sensitive


def set_last_resort(last_resort):
    logging.lastResort = last_resort  # Sensitive


class CustomLogger(Logger):  # Sensitive
    pass


class CustomHandler(Handler):  # Sensitive
    pass


class CustomFilter(Filter):  # Sensitive
    pass


def update_config(path, config):
    fileConfig(path)  # Sensitive
    dictConfig(config)  # Sensitive