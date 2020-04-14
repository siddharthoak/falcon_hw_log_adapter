import logging

from context import ctx


class CustomLogger:

    def setup_custom_logger(self, file_name):
        """Method setup_custom_logger"""
        formatter = logging.Formatter(fmt= \
                '%(asctime)s - %(levelname)s -  %(lineno)s - %(name)s  - %(message)s')

        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        logger = logging.getLogger(file_name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        return logger
