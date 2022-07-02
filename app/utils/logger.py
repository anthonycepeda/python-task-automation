import logging


def set_logger(module):
    """
    This logger function extends from Python loggin module and sets a custom config.
    @params: module name
    @return: logger object
    """

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(message)s]")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(module)
    logger.setLevel(logging.DEBUG)

    logger.addHandler(handler)

    return logger
