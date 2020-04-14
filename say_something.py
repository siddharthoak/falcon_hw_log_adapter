import logging

import custom_logger
from custom_log_adapter import CustomAdapter

cl = custom_logger.CustomLogger()
logger = cl.setup_custom_logger(__name__)
adapter = CustomAdapter(logger, {})


class SaySomething(object):
    def kuch_bolo(self):
        adapter.debug("Kaisa hai")

