import logging

import pytest
from selenium.webdriver.common.by import By

from newwAAPCDEMO.conftest import driver


@pytest.mark.usefixtures("setup1")
class Baseclass1:

    def getlogger(self):
        logger = logging.getLogger(__name__)

        obj_filehandler = logging.FileHandler('logfile.log')  # Filehandler knows in which file logs as to be captured.

        obj_formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s %(message)s")

        obj_filehandler.setFormatter(obj_formatter)

        logger.addHandler(obj_filehandler)  # have to place filehandler object here.
        logger.setLevel(logging.INFO)
        logger.debug("Debug statement is executed")
        logger.info("Information is executed")
        logger.warning("warning message is printed")
        logger.error("error message is printed")
        logger.critical("critical message")
        return logger

