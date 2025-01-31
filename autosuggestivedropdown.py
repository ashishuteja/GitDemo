import time
                                             #use below website for autosuggestive dropdown in conftest file.
                                            #https://rahulshettyacademy.com/dropdownsPractise/
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from tests.conftest import driver
class AutoDropdown:
    def __init__(self, driver):
        self.driver = driver

    def getautosuggdropdown(self):
        driver.find_element(By.ID,"autosuggest").send_keys("IND")
        countries = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a")
        print(len(countries))
        for country in countries:
            if country.text == "India":
                country.click()
                break
        print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))#for random text we use get_attribute method and "value"
        assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
        time.sleep(10)