from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWaitttt

from tests import homepage


@pytest.mark.usefixtures("setup")
class Basecls:
    def verifylinkpresence(self, text):
        element = WebDriverWait(self.driver,10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def seldropdown(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
    pass